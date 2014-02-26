#/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
import pygame

from dame.utils import crop_image


class Sprite(object):

    def __init__(self, filename=None):
        self.filename = filename

    def open(self):
        assert self.filename is not None
        self.src = Image.open(self.filename)
        self.img = pygame.image.frombuffer(
            self.src.tostring(),
            self.src.size,
            self.src.mode).convert()
        return self.img

    def crop(self, size, position):
        cropped_img = crop_image(self.src, size, position)
        img = pygame.image.frombuffer(
            cropped_img.tostring(),
            cropped_img.size,
            croppe_img.mode).convert()
        return img
