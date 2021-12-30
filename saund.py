import pygame

class Saund(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image=pygame.image.load("zvuk_final_1.png").convert_alpha()
        self.rect=self.image.get_rect(center=(x,y))
        pygame.mixer.music.load("white-light.mp3")
        self.pl=True
        pygame.mixer.music.play(-1)
    def update(self, *args):
        self.pl = not self.pl
        if self.pl:
            pygame.mixer.music.unpause()
            self.image=pygame.image.load("zvuk_final_1.png").convert_alpha()
        else:
            pygame.mixer.music.pause()
            self.image=pygame.image.load("zvuk_2_final.png").convert_alpha()
    def adjustment(self,volume):
        print(volume)
        pygame.mixer.music.set_volume(volume)
        if volume<0.1:
           self.image=pygame.image.load("zvuk_2_final.png")
        else:
           self.image=pygame.image.load("zvuk_final_1.png")


