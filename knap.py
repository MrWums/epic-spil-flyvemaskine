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