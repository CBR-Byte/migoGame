import pygame

class Banana_counter:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.problem_font = pygame.font.Font('assets/font/Gamer.ttf', 60)
        self.bananas_counter = 0
        self.banana_image = pygame.image.load("assets/images/banana.png") 
        self.banana_image = pygame.transform.scale(self.banana_image, (50, 50))

    def draw(self, screen, number):
        # Dibujar el contador de bananas en la esquina superior izquierda
        self.bananas_counter = self.problem_font.render(str(number), True, (255, 255, 255))
        text_width, text_height = self.bananas_counter.get_size()
        banana_width, banana_height = self.banana_image.get_size()
        x = self.screen_width*0.26041666666
        y = (2*text_height)
        screen.blit(self.banana_image, (x, y))
        screen.blit(self.bananas_counter, (x + banana_width+10, y))
        pygame.display.update()
    
