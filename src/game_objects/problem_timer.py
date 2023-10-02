import pygame

class Problem_timer:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.problem_font = pygame.font.Font('assets/font/Gamer.ttf', 36)
        self.problem_counter = 0 

    def draw(self, screen, number):
        text = self.problem_font.render(str(number), True, (153, 90, 50))
        text_width, text_height = text.get_size()
        x = (self.screen_width - text_width) // 2
        y = (self.screen_height + 5*text_height) // 2
        screen.blit(text, (x, y))
        pygame.display.update()  # Actualiza la pantalla para mostrar el contador
