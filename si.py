import pygame
import pygame.gfxdraw


def main():
    pygame.init()

    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('példaprogram')

    pygame.gfxdraw.rectangle(felület, téglalap, szín)
    x = 100
    y = 100
    r = 50

    while fut_a_program:
        event = pygame.event.wait()
        if event.type == pygame.VALAMI:
        elif event.type == pygame.MASIK:

    quit = False
    while not quit:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            quit = True


    pygame.quit()