import pygame
pygame.init()

background_image = pygame.image.load('assets/Backgrounds/black.png')
background_image = pygame.transform.scale(background_image, (1080, 720))

space_ship = pygame.image.load('assets/PNG/playerShip1_red.png')
space_ship = pygame.transform.scale_by(space_ship, 0.8)