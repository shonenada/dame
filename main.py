from sys import exit

import pygame
from pygame.locals import *
from dame.app import Dame
from dame.sprite import Sprite


demo = Dame(__name__)
demo.config.from_object('settings')
louis_full = demo.create_sprite('louis_0.bmp')


demo.init()
demo.clr_screen()
louis_full.move_to(50, 50)
louis_full.draw()

pygame.display.update()

demo.loop()
