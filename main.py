from sys import exit

import pygame
from pygame.locals import *
from dame.app import Dame


def print_mouse(event):
    print event.pos


dame = Dame(__name__)
dame.init()
dame.add_listener(MOUSEMOTION, print_mouse)

dame.loop()
