# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:45:18 2017

@author: deron
"""

import pygame, sys
import math
import os
screen = pygame.display.set_mode((1024, 768))
#screen = pygame.display.set_mode((1024, 768), FULLSCREEN)
car = pygame.image.load('download.png')
screen.blit(car, (50, 100))
pygame.display.flip()
rotated  = pygame.transform.rotate(car, 45*math.pi/180)