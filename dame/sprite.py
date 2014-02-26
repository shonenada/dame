#/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
import pygame

from dame.utils import crop_image


class Sprite(object):

    def __init__(self, filename=None, fw=None):
        self.filename = filename
        self.x, self.y = 0, 0
        self.fw = fw

    def open(self):
        self.src = Image.open(self.filename).convert('RGBA')
        self.img = pygame.image.frombuffer(
            self.src.tostring(),
            self.src.size,
            self.src.mode).convert()

    def get(self):
        assert self.filename is not None
        return self.img

    def crop(self, size, position):
        if not hasattr(self, 'src'):
            self.open()
        cropped_img = crop_image(self.src, size, position)
        img = pygame.image.frombuffer(
            cropped_img.tostring(),
            cropped_img.size,
            cropped_img.mode).convert()
        return img

    def move_to(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        if not hasattr(self, 'img'):
            self.open()
        self.fw.screen.blit(self.img, self.position)

    @property
    def position(self):
        return (self.x, self.y)
    @position.setter
    def position(self, value):
        self.x, self.y = value
