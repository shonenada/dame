#/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
import pygame

from dame.utils import crop_image


class Sprite(object):

    def __init__(self, filename=None, fw=None):
        if filename:
            self.open(filename)
            self.convert()
        self.x, self.y = 0, 0
        self.fw = fw

    def open(self, filename):
        self.src = Image.open(filename).convert('RGBA')

    def convert(self):
        self.img = pygame.image.frombuffer(
            self.src.tostring(),
            self.src.size,
            self.src.mode).convert()

    def crop(self, position, size):
        sprite = Sprite(fw=self.fw)
        sprite.src = crop_image(self.src, size, position)
        sprite.convert()
        return sprite

    def move_to(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        self.fw.screen.blit(self.img, self.position)

    @property
    def position(self):
        return (self.x, self.y)
    @position.setter
    def position(self, value):
        self.x, self.y = value
