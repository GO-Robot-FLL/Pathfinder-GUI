
import pygame

from src.object import Object

class Text(Object):

    def __init__(self, x, y, text, fontColor="black"):
        self.x = x
        self.y = y
        self.text = text
        self.fontColor = fontColor
        self.font = pygame.font.SysFont('Verdana', 12, italic=True)

        self.textSurface = self.font.render(self.text, True, self.fontColor)
        self.textRect = self.textSurface.get_rect(center=(self.x, self.y))

        self.objects.append(self)

    def process(self):
        self.screen.blit(self.textSurface, self.textRect)