import pygame
import sys
import os

import pygame_gui

from src.constants import Constants as c
from src.util import Util
from src.map import Map
from src.object import Object
from src.constants import Constants

# setup window 
pygame.display.set_caption("Pathfinder GUI")
pygame.display.set_icon(pygame.image.load(os.path.join(os.getcwd(), "img", "icon.png")))

# initialize objects
map1 = Map()
util = Util()
fpsClock = pygame.time.Clock()
manager = pygame_gui.UIManager((Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH), theme_path=os.path.join(os.getcwd(), "src/themes/themes.json"))

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



# ############################## #
#   Define button objects here   #
# ############################## #

containerButton = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((20, 50), (20, 20)),
                                        starting_height=1,
                                        manager=manager,anchors={'left':'left', 'right':'right', 'top':'top', 'bottom':'bottom'})
containerButton.set_visual_debug_mode(True)


buttonSwitchLeft = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(10, 100, 85, 30),
                                                text='Left',
                                                manager=manager,
                                                container=containerButton)

buttonSwitchRight = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(105, 100, 85, 30),
                                                 text='Right',
                                                 manager=manager,
                                                 container=containerButton)

buttonOutput = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(105, 100, 85, 30),
                                                 text='Right',
                                                 manager=manager,
                                                 container=containerButton)


# selectionSide = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((350, 350), (100, 50)),
#                                                     item_list=['Left', 'Right'],
#                                                     manager=manager)


# Button(1125, 20, 150, 100, 'Output', buttonOutputfunc)
# Button(1125, 140, 65, 65, 'Left', buttonSwitchLeftfunc)
# Button(1210, 140, 65, 65, 'Right', buttonSwitchRightfunc)
# Button(1125, 225, 150, 65, 'Clear Map', buttonClearfunc, "red")


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

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
          if event.ui_element == buttonOutput:
                buttonOutputfunc()

        manager.process_events(event)
    manager.update(fpsClock.tick(c.FPS) / 1000.0)

def run():
    gameloop = True

    # Main loop
    while gameloop:
        Object.screen.fill(c.BACKGROUND_COLOR)
        
        get_events()

        # Display objects on screen
        for object in Object.objects:
            object.process()

        manager.draw_ui(Object.screen)

        # Update 
        pygame.display.flip()
        fpsClock.tick(Constants.FPS)

if __name__ == "__main__":
    run()
    

