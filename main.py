import pygame
from player import player_class

pygame.init()
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()

plane_sprite = pygame.transform.scale_by(pygame.image.load("images/plane.png"),0.5)

player = player_class(display,plane_sprite)

while True:
    clock.tick(60)
    display.fill((6,97,170))

    event = pygame.event.get()

    player.update(event)

    pygame.display.flip()
