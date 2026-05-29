import pygame, sys

screen = pygame.display.set_mode((300, 300))
clock = pygame.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    pygame.display.flip()
