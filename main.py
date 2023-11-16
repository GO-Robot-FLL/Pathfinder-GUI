import pygame
import sys
import os

from src.constants import Constants as c
from src.util import Util
from src.map import Map
from src.button import Button
from src.object import Object

pygame.display.set_caption("Pathfinder GUI")
pygame.display.set_icon(pygame.image.load(os.getcwd() + r"\img\icon.png"))

map1 = Map()
util = Util()
fpsClock = pygame.time.Clock()


def button1func():
    util.printCommands(map1.coordinates, map1)

def button2func():
    global map1
    map1.clear_map()
    del map1
    map1 = Map()

def button3func():
    map1.switch_start()

Button(1125, 20, 150, 100, 'Output', button1func)
Button(1125, 140, 150, 65, 'Clear Map', button2func, "red")
Button(1125, 225, 65, 65, 'Left', print)
Button(1210, 225, 65, 65, 'Right', button3func)


def get_events():
    for event in pygame.event.get():

        # Exit Pathfinder
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Place Point 
        mx, my = pygame.mouse.get_pos()
        inbounds = mx <= map1.MAP_WIDTH_PX and my <= map1.MAP_HEIGHT_PX
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and inbounds:
            map1.coordinates[map1.current_round].append(list(event.pos))

        # Switch round
        if event.type == pygame.KEYDOWN  and pygame.K_1 <= event.key <= pygame.K_6:
            map1.current_round = event.key - pygame.K_1


def run():
    gameloop = True
    fps = 60

    while gameloop:
        Object.screen.fill(c.BACKGROUND_COLOR)
        
        get_events()

        for object in Object.objects:
            object.process()
        
        # Update 
        pygame.display.flip()
        fpsClock.tick(fps)
    
if __name__ == "__main__":
    run()
    

