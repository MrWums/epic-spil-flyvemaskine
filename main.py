import pygame
from player import player_class
from map import map_class

pygame.init()
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()

plane_sprite = pygame.transform.scale_by(pygame.image.load("images/plane.png"),0.5)
tower_sprite = pygame.image.load("images/tower.png")
ground_sprite = pygame.image.load("images/ground.png")

player = player_class(display,plane_sprite)
map = map_class(display,tower_sprite,ground_sprite,(1000,screenheight-150),(1000,100))

while True:
    clock.tick(60)
    display.fill((6,97,170))
    event = pygame.event.get()

    player.update(event)
    map.update()

    pygame.display.flip()
