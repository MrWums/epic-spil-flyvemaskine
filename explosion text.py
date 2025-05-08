import pygame

pygame.init()
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()

class explosion_class(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(3):
            img = pygame.image.load(f"images/explosion{i+1}.png")
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0

    def update(self):
        explosion_speed = 4

        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

explosion_group = pygame.sprite.Group()

while True:
    clock.tick(60)
    display.fill((255,255,255))

    explosion_group.draw(display)
    explosion_group.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                explosion = explosion_class(100,100)
                explosion_group.add(explosion)

    pygame.display.flip()