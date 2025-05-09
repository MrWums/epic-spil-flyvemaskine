import pygame
class knap_class:
   def __init__(self,x,y,width,height,text,font,textcolor):
       self.font = font
       self.textcolor = textcolor
       self.text = text
       self.rect = pygame.Rect(x-width/2,y-height/2,width,height)

   def draw(self,display):
       pygame.draw.rect(display, (150, 192, 192), self.rect)
       text_surface = self.font.render(self.text, True, self.textcolor)
       text_rect = text_surface.get_rect(center=self.rect.center)
       display.blit(text_surface, text_rect)

   def klik(self,event):
       if event.type == pygame.MOUSEBUTTONDOWN:
           if self.rect.collidepoint(event.pos):
               return True
       return False

class explosion_class(pygame.sprite.Sprite):
    sound_played = False
    def __init__(self,x,y,scale_factor):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(3):
            img = pygame.transform.scale_by(pygame.image.load(f"assets/explosion{i + 1}.png"),scale_factor)
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x*scale_factor,y)
        self.counter = 0

    def update(self):
        explosion_speed = 10

        self.counter += 1
        if self.sound_played == False:
            exp_sound = pygame.mixer.Sound("assets/big explosion.wav")
            exp_sound.set_volume(0.05)
            exp_sound.play()
            self.sound_played = True

        if self.counter >= explosion_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


def text(display,x,y,text,font,text_color,background_color):
    text = font.render(text, True, text_color, background_color)
    textRect = text.get_rect()
    textRect.center = (x,y)
    display.blit(text,textRect)