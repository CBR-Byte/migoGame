import pygame
import random

class Banana:
    def __init__(self, screen_width, screen_height, nivel):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.banana_img = pygame.image.load('assets/banana.png')
        self.banana_img = pygame.transform.scale(self.banana_img, (50, 50))
        self.banana_rect = self.banana_img.get_rect()
        self.banana_rect.x = random.randint(500, 1400)  # Posición horizontal aleatoria
        self.banana_rect.y = 200  # Inicia desde la parte superior de la pantalla
        self.speed = 10*nivel  # Velocidad de caída, puedes ajustarla según lo necesites

    def update(self):
        self.banana_rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.banana_img, self.banana_rect)
