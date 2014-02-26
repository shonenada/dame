from sys import exit

import pygame
from pygame.locals import *
from dame.app import Dame
from dame.sprite import Sprite


demo = Dame(__name__)
demo.config.from_object('settings')
demo.init()

louis_full = demo.create_sprite('louis_0.bmp')

demo.clr_screen()

louis_stand = louis_full.crop((0, 0), (80, 80))
louis_stand.move_to(0, 0)
louis_stand.draw()

pygame.display.update()

demo.loop()
