import pygame

class Cursor(pygame.sprite.Sprite):
     def __init__(self,x,y):
         self.image=pygame.image.load("m_ruka_kulak .png").convert_alpha()
         self.rect=self.image.get_rect(center=(x-19,y+30))
         self.pos=pygame.mouse.get_pos()
     def Tip_off(self,pl):
         if pl:
             self.image=pygame.image.load("m_ruka_palets.png").convert_alpha()
         else:
             self.image=pygame.image.load("m_ruka_kulak .png").convert_alpha()
     def update(self,posx,posy):
         self.rect = self.image.get_rect(center=(posx+8, posy+22))

