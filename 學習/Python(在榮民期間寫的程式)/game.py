import sys

import pygame
from pygame.locals import QUIT

pygame.init()

windows_surface = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World')
windows_surface.fill((255,255,255))

head_font = pygame.font.SysFont(None, 60)

text_surface = head_font.render('Hello World!', True, (0, 0, 0))

windows_surface.blit(text_surface, (10, 10))

pygame.display.update()

