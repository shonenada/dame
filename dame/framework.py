#/usr/bin/env python
from __future__ import division
import os
from sys import exit
import time

from PIL import Image
import pygame
from pygame.locals import *

from dame.sprite import Sprite
from dame.utils import import_string, get_root_path, string_types
from dame import colors


class BaseFramework(object):
    
    def __init__(self, import_name, **kwargs):
        self.import_name = import_name
        self.root_path = get_root_path(import_name)

        config = {}
        config.setdefault('CAPTION', 'Dame')
        config.setdefault('SCREEN_WIDTH', 800)
        config.setdefault('SCREEN_HEIGHT', 600)
        config.setdefault('MODE', 0)
        config.setdefault('DEPTH', 8)
        config.setdefault('SPRITE_FOLDER', './')

        if 'caption' in kwargs:
            config['CAPTION'] = kwargs.pop('caption')

        if 'screen_width' in kwargs:
            config['SCREEN_WIDTH'] = kwargs.pop('screen_width')

        if 'screen_height' in kwargs:
            config['SCREEN_HEIGHT'] = kwargs.pop('screen_height')

        if 'mode' in kwargs:
            config['MODE'] = kwargs.pop('mode')

        if 'depth' in kwargs:
            config['DEPTH'] = kwargs.pop('depth')

        if 'sprite_folder' in kwargs:
            config['SPRITE_FOLDER'] = kwargs.pop('sprite_folder')

        self.config = Config(root_path=self.root_path, defaults=config)

        listeners = {}
        if 'listeners' in kwargs:
            listeners = kwargs.pop('listeners')
        self.listener = Listener(listeners)

        self.sprites = []
        pygame.init()

    def init(self):
        pygame.display.set_caption(self.config.get('CAPTION'))
        self.screen = pygame.display.set_mode(
            (self.config['SCREEN_WIDTH'], self.config['SCREEN_HEIGHT']),
            self.config['MODE'], self.config['DEPTH'])

    def clr_screen(self):
        self.screen.fill(colors.WHITE)
        pygame.display.update()

    def create_sprite(self, filepath):
        sprite = Sprite(
            os.path.join(
                self.root_path,
                self.config['SPRITE_FOLDER'],
                filepath), fw=self)
        return sprite

    def add_listener(self, type, action):
        if callable(action):
            self.listener.add(type, action)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

                for action in self.listener[event.type]:
                    action(event)


class Config(dict):

    def __init__(self, root_path, defaults=None):
        dict.__init__(self, defaults or {})
        self.root_path = root_path

    def from_pyfile(self, filename):
        filename = os.path.join(self.root_path, filename)
        d = imp.new_module('config')
        d.__file__ = filename
        try:
            with open(filename) as config_file:
                exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
        except IOError as e:
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise
        self.from_object(d)
        return True

    def from_object(self, obj):
        if isinstance(obj, string_types):
            obj = import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)


class Listener(object):

    ALLOWED = (QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION,
               MOUSEBUTTONDOWN, MOUSEBUTTONUP, JOYAXISMOTION,
               JOYBALLMOTION, JOYHATMOTION, JOYBUTTONDOWN,
               JOYBUTTONUP, VIDEORESIZE, VIDEOEXPOSE, USEREVENT)

    def __init__(self, defaults=None):
        self.listeners = {key: set() for key in self.ALLOWED}

    def add(self, type, action):
        if type in self.ALLOWED and callable(action):
            self.listeners[type].add(action)

    def __getitem__(self, key):
        return self.listeners[key]

    def remove(self, type, action):
        self.listeners[type].discard(action)

    def clear(self):
        listeners = {key: [] for key in self.ALLOWED}
