import pygame
class Start(pygame.sprite.Sprite):
      def __init__(self,x,y):
          self.image=pygame.image.load("igrat.png").convert_alpha()
          self.rect=self.image.get_rect(center=(x/2,y/2))
      def p(self,f):
          if f:
             self.image=pygame.image.load("igrat_2.png").convert_alpha()
          else:
             self.image=pygame.image.load("igrat.png").convert_alpha()