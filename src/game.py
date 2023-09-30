import pygame
import sys
import math
import random
from game_objects.migo import Migo
from game_objects.problem import Problem
from game_objects.problem_timer import Problem_timer
from game_objects.game_timer import Game_timer
from game_objects.banana_counter import Banana_counter
from game_objects.banana import Banana

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.migo = Migo(screen_width, screen_height)
        self.timer_problem = Problem_timer(screen_width, screen_height)
        self.timer_game = Game_timer(screen_width, screen_height)
        self.banana_counter = Banana_counter(screen_width, screen_height)
        self.clock = pygame.time.Clock()
        self.problem = Problem(screen_width, screen_height)
        self.bananas = []
        self.bananas_gotten = []
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.problem_timer = 5
        self.problem_time = 0
        self.problem_visible = True
        self.game_timer = 60
        self.game_time = 0
        self.problem_generated = False
        self.level = 1
        self.win = False
        self.lose = False
        self.lose_text = self.font.render("Ganaste", True, (255, 255, 255))
        self.win_text = self.font.render("Ganaste", True, (255, 255, 255))

    def run(self, screen):
        running = True
        while running:

            while not self.win and not self.lose:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()

                # Mostrar el problema 5 segundos
                if self.problem_visible:
                    self.timer_problem.draw(screen, math.ceil(self.problem_timer - self.problem_time))
                    self.problem_time += self.clock.tick() / 1000
                    if not self.problem_generated:
                        self.problem.generate_problem() 
                        self.problem_generated = True 
                    if self.problem_time >= self.problem_timer:
                        self.problem_visible = False
                        self.problem_time = 0
            
                # Mostrar el tiempo restante
                else:
                    if self.game_time <= self.game_timer:
                        self.timer_game.draw(screen, math.ceil(self.game_timer - self.game_time))
                        self.game_time += self.clock.tick() / 1000
                        print(len(self.bananas_gotten))
                        self.banana_counter.draw(screen, len(self.bananas_gotten))
                        if random.randint(0, 100) < 10:  
                            self.bananas.append(Banana(self.screen_width, self.screen_height, self.level))
                    else:
                        if self.problem.answer == len(self.bananas_gotten):
                            self.lose = True
                            self.game_time = 0
                            self.problem_time = 0
                            self.problem_visible = True
                            self.problem_generated = False
                            self.bananas = []
                            self.bananas_gotten = []
                            self.level += 1
                        else:
                            self.win = False
                            self.game_time = 0
                            self.problem_time = 0
                            self.problem_visible = True
                            self.problem_generated = False
                            self.bananas = []
                            self.bananas_gotten = []
                            self.level = 1
                    
                # Movimiento del personaje
                keys = pygame.key.get_pressed()

                if keys[pygame.K_RIGHT]:
                    self.migo.move(1)
                elif keys[pygame.K_LEFT]:
                    self.migo.move(-1)
                else:
                    self.migo.move(0)

                # Colisiones
                # Aumentar el contador de bananas
                self.bananas_gotten.extend([banana for banana in self.bananas if self.migo.x < banana.banana_rect.x + banana.banana_rect.width and
                            self.migo.x + self.migo.width > banana.banana_rect.x and
                            self.migo.y < banana.banana_rect.y + banana.banana_rect.height and
                            self.migo.y + self.migo.height > banana.banana_rect.y])

                # Eliminar bananas que colisionan con el personaje
                self.bananas = [banana for banana in self.bananas if not (self.migo.x < banana.banana_rect.x + banana.banana_rect.width and
                            self.migo.x + self.migo.width > banana.banana_rect.x and
                            self.migo.y < banana.banana_rect.y + banana.banana_rect.height and
                            self.migo.y + self.migo.height > banana.banana_rect.y)]
                
                # Eliminar bananas que llegan al suelo
                for banana in self.bananas:
                    if banana.banana_rect.y >= self.screen_height - 180:
                        self.bananas.remove(banana)
                

                screen.fill((0, 0, 0)) 
            
                background_image = pygame.image.load("assets/background.png")
                original_width, original_height = background_image.get_size()
                aspect_ratio = original_width / original_height
                new_height = self.screen_height
                new_width = int(new_height * aspect_ratio)
                background_image = pygame.transform.scale(background_image, (new_width, new_height))
                x = (self.screen_width - new_width) // 2
                y = (self.screen_height - new_height) // 2
                screen.fill((0, 0, 0)) 
                screen.blit(background_image, (x, y))
                if self.problem_visible:
                    self.problem.draw(screen)
                else:
                    self.migo.draw(screen)
                    for banana in self.bananas:
                        banana.draw(screen)
                    for banana in self.bananas:
                        banana.update()
                pygame.display.update()
                pygame.time.Clock().tick(250) 

            if self.win:
                self.win = False
                espera = 10
                while espera > 0:
                    background_image = pygame.image.load("assets/background.png")
                    original_width, original_height = background_image.get_size()
                    aspect_ratio = original_width / original_height
                    new_height = self.screen_height
                    new_width = int(new_height * aspect_ratio)
                    background_image = pygame.transform.scale(background_image, (new_width, new_height))
                    x = (self.screen_width - new_width) // 2
                    y = (self.screen_height - new_height) // 2
                    screen.fill((0, 0, 0)) 
                    screen.blit(background_image, (x, y))
                    screen.blit(self.win_text, (self.screen_width//2, self.screen_height//2))
                    pygame.display.update()
                    espera -= 1
                    pygame.time.Clock().tick(250)
            else:
                self.lose = False
                espera = 10
                while espera > 0:
                    background_image = pygame.image.load("assets/background.png")
                    original_width, original_height = background_image.get_size()
                    aspect_ratio = original_width / original_height
                    new_height = self.screen_height
                    new_width = int(new_height * aspect_ratio)
                    background_image = pygame.transform.scale(background_image, (new_width, new_height))
                    x = (self.screen_width - new_width) // 2
                    y = (self.screen_height - new_height) // 2
                    screen.fill((0, 0, 0)) 
                    screen.blit(background_image, (x, y))
                    screen.blit(self.lose_text, (self.screen_width//2, self.screen_height//2))
                    pygame.display.update()
                    espera -= 1
                    pygame.time.Clock().tick(250)
