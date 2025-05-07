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

player = player_class(display,plane_sprite,screenheight)

map = map_class(display,tower_sprite,ground_sprite,(0,screenheight-100),(2500,100))

while True:
    clock.tick(60)
    display.fill((6,97,170))
    event = pygame.event.get()

    player_pos = pygame.Vector2(player.update(event))
    map_pos = pygame.Vector2(map.update())

    if player_pos.x >= map_pos.x:
        print("yeet")

    for i in range(10):
        map.draw(i)

    pygame.display.flip()
