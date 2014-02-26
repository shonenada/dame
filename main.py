from sys import exit

import pygame
from pygame.locals import *
from dame.app import Dame


demo = Dame(__name__)
demo.config.from_object('settings')
demo.init()
demo.clr_screen()
demo.new_sprite('dennis', 'dennis_0.bmp')
demo.put_sprite('dennis', (0, 0), (80, 80), (0, 0))
pygame.display.update()

demo.loop()
