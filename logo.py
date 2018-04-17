# ICS3U
# Assignment 2: Logo
# <your name>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
import math
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (29, 185, 84)
RED = (255, 0, 0)
BLUE = (62, 68, 182)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    # Clear the screen to white
    screen.fill(BLACK)
    
    # --- Draw code goes here
    pygame.draw.ellipse(screen, GREEN, [50, 50, 300,300], 0)
    pygame.draw.ellipse(screen, BLACK, [102, 135, 25, 25],0)
    pygame.draw.arc(screen, BLACK, [100,117,200,80],math.radians(0),math.radians(173),25)
    pygame.draw.ellipse(screen, BLACK, [278,143,25,25],0)
    pygame.draw.arc(screen,BLACK,[100, 160, 200,80,], math.radians(30), math.radians(153), 20)
    pygame.draw.ellipse(screen, BLACK, [112,175,20,20],0)
    pygame.draw.ellipse(screen,BLACK, [268,176,20,20],0)
    pygame.draw.arc(screen,BLACK,[100,200,200,80], math.radians(43), math.radians(143), 15)
    pygame.draw.ellipse(screen,BLACK,[120, 220,16,16],0)
    pygame.draw.ellipse(screen,BLACK,[260, 218,16,16],0)
    

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    #pygame.draw.line(screen,WHITE, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
    
    #pygame.draw.line(screen, WHITE, [42,10], [200,200], 5) 
        # Update the screen with queued shape.s
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
