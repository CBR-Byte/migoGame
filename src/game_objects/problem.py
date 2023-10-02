import pygame
import random

class Problem:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font('assets/font/Gamer.ttf', 80)
        self.problem = ""
        self.answer = 0
        self.problem_text = self.font.render(self.problem, True, (153, 90, 50))
    
    def generate_problem(self): # Funcion que genera un problema aleatorio se escojen 2 numeros del 1 al 10 y un operador aleatorio de suma o resta
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.choice(["+", "-"])
        if c == "+":
            self.answer = a + b
            self.problem = f'{a} {c} {b}'
        elif c == "-":
            if a < b: # Si el primer numero es menor que el segundo, se intercambian los numeros para que el resultado sea positivo
                a, b = b, a
            self.problem = f'{a} {c} {b}'
            self.answer = a - b

    def draw(self, screen):
        problem_surface = self.font.render(self.problem, True, (153, 90, 50))
        text_width, text_height = problem_surface.get_size()
        x = (self.screen_width - text_width) // 2
        y = (self.screen_height - text_height) // 2
        screen.blit(problem_surface, (x, y)) # Dibujar el problema en el centro de la pantalla
        
    def check_answer(self, answer): # Funcion que verifica si la respuesta es correcta
        if answer == self.answer:
            self.generate_problem()
            return True
        else:
            return False