import pygame

class map_class:
    speed = 5
    def __init__(self,display,tower_image,ground_image,ground_position,tower_position):
        self.display = display
        self.ground_pos = pygame.Vector2(ground_position)
        self.tower_pos = pygame.Vector2(tower_position)
        self.tower = tower_image
        self.ground = ground_image

    def update(self):
        self.ground_pos.x -= self.speed
        self.tower_pos.x -= self.speed
        self.draw()

    def draw(self):
        self.display.blit(self.ground,self.ground_pos)
        self.display.blit(self.tower,self.tower_pos)
