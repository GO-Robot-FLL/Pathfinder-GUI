import pygame
from src.constants import Constants as c

"""
Parent class for every Object on screen
"""

class Object:
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    font = pygame.font.SysFont('Verdana', 16)

    objects = []
    
