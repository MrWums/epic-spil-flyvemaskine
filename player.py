import pygame

class player_class:
    speed = 3
    gravity = 1
    jumping = False
    def __init__(self,display,image,y):
        self.x = 100
        self.y = y/2
        self.ground = y-100
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

        # Y-akse movement stuff
        if self.jumping == True:
            self.velocity -= self.speed

        # Dark magic
        self.y += self.velocity
        if self.y >= self.ground:
            self.velocity = 0
            self.y = self.ground
        else:
            self.velocity += self.gravity

        self.draw()
    def draw(self):
        self.display.blit(self.image,(self.x,self.y))
