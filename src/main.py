import pygame

# intial instances of pygame
pygame.init()

screen = pygame.display.set_mode((800,600))


running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

