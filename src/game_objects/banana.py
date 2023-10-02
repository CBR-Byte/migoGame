import pygame
import random
import math

class Banana:
    def __init__(self, screen_width, screen_height, nivel):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.banana_img = pygame.image.load('assets/images/banana.png')
        self.banana_img = pygame.transform.scale(self.banana_img, (50, 50))
        self.banana_rect = self.banana_img.get_rect()
        self.banana_rect.x = random.randint(math.ceil(screen_width*0.26041666666), math.ceil(screen_width*0.72916666666))
        self.banana_rect.y = 200
        self.speed = 15 + nivel*5

    def update(self):
        # Mover la banana hacia abajo
        self.banana_rect.y += self.speed

    def draw(self, screen):
        # Dibujar la banana en la pantalla
        screen.blit(self.banana_img, self.banana_rect)
