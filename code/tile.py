import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/test/rock.png").convert_alpha()
        self.size = self.image.get_size()
        self.bigger_image = pygame.transform.scale(self.image, (int(self.size[0]*SCALEFACTOR), int(self.size[1]*SCALEFACTOR)))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(48,38)