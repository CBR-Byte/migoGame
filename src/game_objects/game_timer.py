import pygame

class Game_timer:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.problem_font = pygame.font.Font(None, 60)  # Choose a suitable font
        self.problem_counter = 0 

    def draw(self, screen, number):
        text = self.problem_font.render(str(number), True, (255, 255, 255))
        text_width, text_height = text.get_size()
        x = (self.screen_width - text_width) // 2
        y = (2*text_height) 
        screen.blit(text, (x, y))
        pygame.display.update()  # Actualiza la pantalla para mostrar el contador
