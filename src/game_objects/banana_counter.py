import pygame

class Banana_counter:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.problem_font = pygame.font.Font(None, 60)  # Choose a suitable font
        self.bananas_counter = 0
        self.banana_image = pygame.image.load("assets/banana.png") 
        self.banana_image = pygame.transform.scale(self.banana_image, (50, 50))  # Ajusta el tamaño de la imagen de la banana

    def draw(self, screen, number):
        self.bananas_counter = self.problem_font.render(str(number), True, (255, 255, 255))
        text_width, text_height = self.bananas_counter.get_size()
        banana_width, banana_height = self.banana_image.get_size()

        # Calcula las posiciones para centrar verticalmente la imagen con el texto
        x = 500
        y = (2*text_height)

        # Dibuja la imagen de la banana a la izquierda del texto
        screen.blit(self.banana_image, (x, y-10))
        # Dibuja el texto del contador a la derecha de la imagen
        screen.blit(self.bananas_counter, (x + banana_width+10, y))
        pygame.display.update()  # Actualiza la pantalla para mostrar el contador con la imagen centrada verticalmente
    
