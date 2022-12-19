import sys

import pygame

from raindrop import Raindrop

def get_number_raindrops_x(raindrops_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = raindrops_settings.screen_width - 2 * raindrop_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def get_number_rows(raindrops_settings, raindrop_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (raindrops_settings.screen_height - raindrop_height)
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def create_raindrop(raindrops_settings, screen, raindrops, raindrop_number, row_number):
    raindrop = Raindrop(raindrops_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
    raindrops.add(raindrop)    
       
def create_grid(raindrops_settings, screen, raindrops):
    """Create a full grid of raindrops."""
    # Create a raindrop and find the number of raindrops in a row.
    # Spacing between each raindrop is equal to one raindrop width.
    raindrop = Raindrop(raindrops_settings, screen)
    number_raindrops_x = get_number_raindrops_x(raindrops_settings, raindrop.rect.width)
    number_rows = get_number_rows(raindrops_settings, raindrop.rect.height) ###error here? pg 274
    
    # Create the grid of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(raindrops_settings, screen, raindrops, raindrop_number, row_number)
        

    
def check_events():
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # End the game.
                sys.exit()

def update_screen(raindrops_settings, screen, raindrops):
    """Update images on the screen and flip to then new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(raindrops_settings.bg_color)
    
    # Redraw all the raindrops.
    raindrops.draw(screen)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_raindrops(raindrops):
    """Update the position of all raindrops in the grid."""
    raindrops.update()
