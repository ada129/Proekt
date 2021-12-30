import pygame

class Progress(pygame.sprite.Sprite):
      def __init__(self,level,fork,x,y):
          self.pictures=[["1.png"],["doska_4.png"],["doska_4_5.png","doska_5.png"],["doska_6.png","",],["doska_7.png"]]
          self.image=pygame.image.load(self.pictures[level][fork])
          self.rect=self.image.get_rect(topleft=(0,0))
      def update(self,level,fork):
          self.image=pygame.image.load(self.pictures[level][fork])