import pygame

class player_class:
    speed = 3
    gravity = 0
    jumping = False
    started = False
    def __init__(self,display,image,y):
        self.x = 100
        self.y = y/2
        self.ground = y-235
        self.velocity = 0
        self.display = display
        self.image = image

    def update(self,event):
        for event in event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.jumping = True
                    self.gravity = 1
                    self.started = True

                if event.key == pygame.K_ESCAPE:
                    return "quit"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.jumping = False

        # Y-akse movement stuff
        if self.jumping == True:
            self.velocity -= self.speed

        # Dark magic
        self.y += self.velocity
        if self.y >= self.ground:
            return "dead"
        elif self.y <= 0:
            self.velocity = +0.1
            self.y = 0
        else:
            self.velocity += self.gravity

        self.draw()

        # returnerer koordinaterne til nederst højre hjørne af flyet (roughly)
        return pygame.Vector2(self.x + 446/2, self.y + 271/4)

    def draw(self):
        self.display.blit(self.image,(self.x,self.y))