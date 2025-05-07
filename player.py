import pygame

class player_class:
    speed = 0.025
    gravity = 0.01
    jumping = False
    def __init__(self,display,image):
        self.x = 100
        self.y = 400
        self.ground = self.y
        self.velocity = 0
        self.display = display
        self.image = image

    def update(self,event):
        for event in event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.jumping = True

                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.jumping = False

        if self.jumping == True:
            self.velocity -= self.speed

        self.y += self.velocity
        if self.y >= self.ground:
            self.velocity = 0
            self.y = self.ground
        else:
            self.velocity += self.gravity

        self.draw()
    def draw(self):
        self.display.blit(self.image,(self.x,self.y))
