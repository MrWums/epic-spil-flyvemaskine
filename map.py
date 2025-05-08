import pygame

class map_class:
    speed = 10
    def __init__(self,display,tower_image,ground_image,ground_position,tower_position):
        self.display = display
        self.ground_pos = pygame.Vector2(ground_position)
        self.tower_pos = pygame.Vector2(tower_position)
        self.ground_image = ground_image
        self.tower_image = tower_image
        self.ground_width = 835

    def update(self,started):
        self.ground_pos.x -= self.speed
        if started == True:
            self.tower_pos.x -= self.speed

        return self.tower_pos

    def draw(self,map_number,started):
        self.display.blit(self.ground_image,(self.ground_pos.x+self.ground_width*map_number,self.ground_pos.y))
        if map_number == 0 and started == True:
            self.display.blit(self.tower_image,self.tower_pos)