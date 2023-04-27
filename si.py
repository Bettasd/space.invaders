import pygame
import pygame.gfxdraw


def main():
    # pygame inicializálás
    pygame.init()

    # ablak megnyitás
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('példaprogram')

    # színek
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    x = 100
    y = 100
    r = 50