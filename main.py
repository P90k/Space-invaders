
import pygame
import pymunk
from event_handling import *
from images import *
from gameobjects import *
pygame.init()

# Control frame rate
FPS = pygame.time.Clock()
FPS.tick(60)

def generate_screen():
    """Set up display window"""
    width, height = 1080, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Test")
    return screen


def main(screen):
    """Main loop of the game session"""
    running = True

    # Create spaceship
    ship = SpaceShip(screen, space_ship)
    while running:
        running = handle_events()

        # Generate background image
        screen.blit(background_image, (0,0))
        ship.draw()

        # Update display
        pygame.display.flip()


def game_execution_flow():
    """Control game flow"""
    screen = generate_screen()
    main(screen)

game_execution_flow()