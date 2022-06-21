#!/usr/bin/env python3

# Created by: Noah McCaskill
# Created on: June 2022
# This will display the "Space Aliens" program on EdgeBadge

import ugame
import stage

import constants


def menu_scene():
    # this function is the menu scene 
    
    # this image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    # create a stage for the background to show up on
    # and set the framerate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely I will only render background once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True: 
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()
            
        # update game logic
        game.tick() # wait until refresh rate finishes
        
      
if __name__ == "__main__":
    game_scene()
    
