import pygame
from player import player_class

pygame.init()
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwidth,screenheight))

player = player_class(display, pygame.image.load("images/hveppe.webp"))

while True:
    display.fill((255,255,255))

    event = pygame.event.get()

    player.update(event)

    pygame.display.flip()
