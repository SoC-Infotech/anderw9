#import 2 libraries to our game
import pygame
import random

#initialize the pygame(game, loop, game scene)
pygame.init()

#declare some variable/constants
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Will")

#main program
# create a game loop to keep the window visible
inPlay = True
while inPlay:
    win.fill(GREEN) #make background green
    pygame.display.update()
    pygame.time.delay(100)

#quit the pygame
pygame = quit()