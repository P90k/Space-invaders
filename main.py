
import pygame
from event_handling import *
from images import *
pygame.init()

# Set up display
def generate_screen():
    width, height = 1080, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Test")
    return screen

# Main loop
def main(screen):
    running = True
    while running:
        running = handle_events()

        # Generate background image
        screen.blit(background_image, (0,0))

        # Update display
        pygame.display.flip()


def game_execution_flow():
    """Control game flow"""
    screen = generate_screen()
    main(screen)

game_execution_flow()