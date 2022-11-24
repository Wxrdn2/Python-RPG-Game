import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstical_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/test/player.png").convert_alpha()
        self.size = self.image.get_size()
        self.bigger_image = pygame.transform.scale(self.image, (int(self.size[0]*SCALEFACTOR), int(self.size[1]*SCALEFACTOR)))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(48,22)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstical_sprites = obstical_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center
    
    def collision(self,direction):
        if direction == "horizontal":
           for sprite in self.obstical_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if self.direction.x > 0: # moving right
                    self.hitbox.right = sprite.hitbox.left
                if self.direction.x < 0: # moving left
                    self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
           for sprite in self.obstical_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if self.direction.y > 0: # moving down
                    self.hitbox.bottom = sprite.hitbox.top
                if self.direction.y < 0: # moving up
                    self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)