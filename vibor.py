import pygame

class Vibor(pygame.sprite.Sprite):
    def __init__(self,filename,x,y,numder):
        super().__init__()
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect(center=(x,y))
        self.numder=numder
    def update(self,level):
        if int(level)==self.numder:
          if self.numder==1:
             self.image=pygame.image.load("1_mini.png")
          elif self.numder==2:
             self.image=pygame.image.load("2_mini.png")
          elif self.numder==3:
             self.image=pygame.image.load("nomer_3.png")
          elif self.numder==4:
              self.image=pygame.image.load("nomer_4.png")
          else:
              self.image=pygame.image.load("nomer_5.png")
        else:
            if self.numder!=0 and self.numder<=5:
                self.image=pygame.image.load("krest_12.png")


