import pygame
import sys
import os

from src.constants import Constants as c
from src.util import Util
from src.map import Map
from src.button import Button
from src.object import Object


# Setup window 
pygame.display.set_caption("Pathfinder GUI")
pygame.display.set_icon(pygame.image.load(os.getcwd() + r"\img\icon.png"))


# Initialize objects
map1 = Map()
util = Util()
fpsClock = pygame.time.Clock()



# ############################## #
#  Define button functions here  #
# ############################## #

def buttonOutputfunc():
    util.printCommands(map1.coordinates, map1)

def buttonClearfunc():
    global map1
    map1.clear_map()
    del map1
    map1 = Map()

def buttonSwitchRight():
    map1.switch_start("right")

def buttonSwitchLeft():
    map1.switch_start("left")



# ############################## #
#   Define button objects here   #
# ############################## #

Button(1125, 20, 150, 100, 'Output', buttonOutputfunc)
Button(1125, 140, 65, 65, 'Left', buttonSwitchLeft)
Button(1210, 140, 65, 65, 'Right', buttonSwitchRight)
Button(1125, 225, 150, 65, 'Clear Map', buttonClearfunc, "red")



def get_events():

    # Get events
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

    # Main loop
    while gameloop:
        Object.screen.fill(c.BACKGROUND_COLOR)
        
        get_events()

        # Diplay objects on screen
        for object in Object.objects:
            object.process()
        
        # Update 
        pygame.display.flip()
        fpsClock.tick(fps)
    
if __name__ == "__main__":
    run()
    

