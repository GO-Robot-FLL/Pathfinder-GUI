import pygame
import sys
import os

from src.constants import Constants as c
from src.util import Util
from src.map import Map
from src.button import Button
from src.object import Object


# setup window 
pygame.display.set_caption("Pathfinder GUI")
pygame.display.set_icon(pygame.image.load(os.path.join(os.getcwd(), "img", "icon.png")))


# initialize objects
map1 = Map()
util = Util()
fpsClock = pygame.time.Clock()



# ############################## #
#  Define button functions here  #
# ############################## #

def buttonOutputfunc():
    util.printCommands(map1)

def buttonClearfunc():
    global map1
    map1.clear_map()
    del map1
    map1 = Map()

def buttonSwitchRightfunc():
    map1.switch_start("right")

def buttonSwitchLeftfunc():
    map1.switch_start("left")

# def buttonImportfunc():
#     util.importCoords(map1)

# def buttonExportfunc():
#     util.exportCoords(map1)

# ############################## #
#   Define button objects here   #
# ############################## #

Button(1125, 20, 150, 100, 'Output', buttonOutputfunc)
Button(1125, 140, 65, 65, 'Left', buttonSwitchLeftfunc)
Button(1210, 140, 65, 65, 'Right', buttonSwitchRightfunc)
Button(1125, 225, 150, 65, 'Clear Map', buttonClearfunc, "red")
# Button(1125, 450, 150, 65, 'Import', buttonImportfunc)
# Button(1125, 535, 150, 65, 'Export', buttonExportfunc)


def get_events():

    # get events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Place point 
        mx, my = pygame.mouse.get_pos()
        inbounds = mx <= map1.MAP_WIDTH_PX and my <= map1.MAP_HEIGHT_PX
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and inbounds:
            map1.coordinates[map1.current_round].append(list(event.pos))

        # Switch round
        if event.type == pygame.KEYDOWN and pygame.K_1 <= event.key <= pygame.K_6:
            map1.current_round = event.key - pygame.K_1

def run():
    gameloop = True
    fps = 60

    # Main loop
    while gameloop:
        Object.screen.fill(c.BACKGROUND_COLOR)
        
        get_events()

        # Display objects on screen
        for object in Object.objects:
            object.process()
        
        # Update 
        pygame.display.flip()
        fpsClock.tick(fps)
    
if __name__ == "__main__":
    run()
    

