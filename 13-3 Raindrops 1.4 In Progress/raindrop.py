import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop on the window."""
    
    def __init__(self, raindrops_settings, screen):
        """Initialize the raindrop and set its starting position."""
        super(Raindrop, self).__init__()
        self.screen = screen
        self.raindrops_settings = raindrops_settings
        
        # Load the raindrop image and get its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new raindrop near top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the raindrop's exact position.
        self.y = float(self.rect.y)
        
    # ~ def blitme(self):
        # ~ """Draw the raindrop at its current location."""
        # ~ self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the raindrop down."""
        self.y += self.raindrops_settings.raindrop_speed_factor
        self.rect.y = self.y
