import pygame
import os

from src.constants import Constants as c 
from src.object import Object


class Map(Object):

    def __init__(self):
        
        self.mapSurf = pygame.transform.scale(pygame.image.load(os.getcwd() + r"\img\map.jpg"), (1100, 622))

        self.MAP_HEIGHT_PX = self.mapSurf.get_height()
        self.MAP_WIDTH_PX = self.mapSurf.get_width()
        self.MAP_WIDTH_CM = 201
        self.MAP_HEIGHT_CM = 113.5

        self.X_SCALE = self.MAP_WIDTH_CM / self.MAP_WIDTH_PX
        self.Y_SCALE = self.MAP_HEIGHT_CM / self.MAP_HEIGHT_PX

        self.current_round = 0
        self.START_CORDS = [55, self.MAP_HEIGHT_PX - 20]
        self.coordinates = [[self.START_CORDS] for _ in range(c.ROUND_NUM)]
        
        self.objects.append(self)

    
    def clear_map(self):
        print("==== Map cleared! ====")
        self.coordinates = [[self.START_CORDS] for _ in range(c.ROUND_NUM)]

        
    def switch_start(self):
        
        self.coordinates[self.current_round][0] = [900, self.MAP_HEIGHT_PX - 20]



    def process(self):

        # Enumerate every round 
        for color_index, round_coords in enumerate(self.coordinates):

            color = c.LINE_COLORS[color_index]

            # Draw start
            pygame.draw.circle(self.mapSurf, c.LINE_COLORS[self.current_round], round_coords[0], c.POINT_RADIUS)
            
            # Draw path
            for i in range(1, len(round_coords)):
                pygame.draw.line(self.mapSurf, color, round_coords[i - 1], round_coords[i], width=3)
                pygame.draw.circle(self.mapSurf, color, round_coords[i], c.POINT_RADIUS)
            
        self.screen.blit(self.mapSurf, (0, 0))