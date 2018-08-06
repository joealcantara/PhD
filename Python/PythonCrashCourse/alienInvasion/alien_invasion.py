import sys
import pygame

from settings import Settings

def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set background colour.
    bg_colour = (230, 230, 230)

    # Start main loop for the game.
    while True:

        # Watch for Keyboard and Mouse Events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_colour)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()