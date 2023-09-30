import pygame
import random

class Problem:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font('freesansbold.ttf', 80)
        self.problem = ""
        self.answer = 0
        self.problem_text = self.font.render(self.problem, True, (255, 255, 255))
    
    def generate_problem(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.choice(["+", "-"])
        if c == "+":
            self.answer = a + b
            self.problem = f'{a} {c} {b}'
        elif c == "-":
            if a < b:
                a, b = b, a
            self.problem = f'{a} {c} {b}'
            self.answer = a - b

    def draw(self, screen):
        problem_surface = self.font.render(self.problem, True, (255, 255, 255))
        text_width, text_height = problem_surface.get_size()
        x = (self.screen_width - text_width) // 2
        y = (self.screen_height - text_height) // 2
        screen.blit(problem_surface, (x, y))
        
    def check_answer(self, answer):
        if answer == self.answer:
            self.generate_problem()
            return True
        else:
            return False