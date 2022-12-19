import pygame

from pygame.sprite import Group
from settings import Settings
from raindrop import Raindrop
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and a screen object.
    pygame.init()
    raindrops_settings = Settings()
    screen = pygame.display.set_mode((raindrops_settings.screen_width,
                                    raindrops_settings.screen_height))
    pygame.display.set_caption("Raindrops")
    
    # Make a raindrop.
    raindrops = Group()
    
    # Create a grid of raindrops.
    gf.create_grid(raindrops_settings, screen, raindrops)
    
    # Start the main loop for the game.
    while True:
        
        gf.check_events()
        gf.update_raindrops(raindrops)
        gf.update_screen(raindrops_settings, screen, raindrops)

        
run_game()
