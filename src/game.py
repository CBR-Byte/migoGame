import pygame
import sys
import math
import random
from src.game_objects.migo import Migo
from src.game_objects.problem import Problem
from src.game_objects.problem_timer import Problem_timer
from src.game_objects.game_timer import Game_timer
from src.game_objects.banana_counter import Banana_counter
from src.game_objects.banana import Banana
import pygame.mixer

class Game: # Clase que representa el juego
    def __init__(self, screen_width, screen_height): # Constructor de la clase
        pygame.mixer.init()
        self.timer_sound = pygame.mixer.Sound("assets/sounds/timer.mp3")
        self.banana_sound = pygame.mixer.Sound("assets/sounds/banana.ogg")
        self.game_sound = pygame.mixer.Sound("assets/sounds/KevinMacLeod-IttyBitty8Bit.mp3")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.migo = Migo(screen_width, screen_height) # Se crea el personaje
        self.timer_problem = Problem_timer(screen_width, screen_height) # Se crea el timer del problema
        self.timer_game = Game_timer(screen_width, screen_height) # Se crea el timer del juego
        self.banana_counter = Banana_counter(screen_width, screen_height) # Se crea el contador de bananas
        self.clock = pygame.time.Clock()
        self.problem = Problem(screen_width, screen_height)
        self.bananas = [] # Lista de bananas
        self.bananas_gotten = [] # Lista de bananas que el personaje ha agarrado
        self.font = pygame.font.Font('assets/font/Gamer.ttf', 80)
        self.problem_timer = 5
        self.problem_time = 0
        self.problem_visible = True
        self.game_timer = 60
        self.game_time = 0
        self.problem_generated = False
        self.level = 1
        self.win = False
        self.lose = False
        self.lose_text = self.font.render("Perdiste", True, (153, 90, 50))
        self.lose_sound = pygame.mixer.Sound("assets/sounds/lose.ogg")
        self.win_text = self.font.render("Ganaste", True, (153, 90, 50))
        self.win_sound = pygame.mixer.Sound("assets/sounds/win.ogg")

    def run(self, screen): # Funcion que ejecuta el juego
        running = True # Variable que indica si el juego esta corriendo
        flag = True # Variable que indica si se debe reproducir el sonido del timer
        flag2 = True # Variable que indica si se debe reproducir el sonido del juego
        while running:
            while not self.win and not self.lose:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()

                # Mostrar el problema 5 segundos
                if self.problem_visible:
                    if flag:
                        self.timer_sound.play() # Reproducir el sonido del timer
                        flag = False
                    self.timer_problem.draw(screen, math.ceil(self.problem_timer - self.problem_time))
                    self.problem_time += self.clock.tick() / 1000 # Actualizar el tiempo del problema
                    if not self.problem_generated: 
                        self.problem.generate_problem() # Generar el problema si no se ha generado
                        self.problem_generated = True 
                    if self.problem_time >= self.problem_timer: # Si el tiempo del problema es mayor o igual al tiempo del timer, se oculta el problema
                        self.problem_visible = False
                        self.problem_time = 0
            
                # Mostrar el tiempo restante
                else:
                    self.timer_sound.stop()
                    if flag2:
                        self.game_sound.play() # Reproducir el sonido del juego
                        flag2 = False
                    if self.game_time <= self.game_timer: # Si el tiempo del juego es menor o igual al tiempo del timer, se muestra el tiempo restante
                        self.timer_game.draw(screen, math.ceil(self.game_timer - self.game_time))
                        self.game_time += self.clock.tick() / 1000
                        self.banana_counter.draw(screen, len(self.bananas_gotten)) # Se dibuja el contador de bananas
                        if random.randint(0, 100) < 15: # Se genera una banana con una probabilidad del 15%
                            self.bananas.append(Banana(self.screen_width, self.screen_height, self.level)) # Se agrega la banana a la lista de bananas
                    else:
                        # Si el tiempo del juego es mayor al tiempo del timer, se verifica si el jugador gano o perdio
                        if self.problem.answer == len(self.bananas_gotten): # Si el jugador respondio correctamente, gana y avanzara al siguiente nivel, sino, pierde y lo lleva al menú
                            self.win = True
                            self.game_sound.stop()
                        else:
                            self.game_sound.stop()
                            self.lose = True
                    
                # Movimiento del personaje
                keys = pygame.key.get_pressed()

                if keys[pygame.K_RIGHT]: # Si se presiona la flecha derecha, el personaje se mueve a la derecha
                    self.migo.move(1)
                elif keys[pygame.K_LEFT]: # Si se presiona la flecha izquierda, el personaje se mueve a la izquierda
                    self.migo.move(-1)
                else: # Si no se presiona ninguna flecha, el personaje se queda quieto
                    self.migo.move(0)

                # Colisiones
                # Aumentar el contador de bananas si el personaje colisiona con una banana
                self.bananas_gotten.extend([banana for banana in self.bananas if self.migo.x < banana.banana_rect.x + banana.banana_rect.width and
                            self.migo.x + self.migo.width > banana.banana_rect.x and
                            self.migo.y < banana.banana_rect.y + banana.banana_rect.height and
                            self.migo.y + self.migo.height > banana.banana_rect.y])
                
                # Reproducir sonido de banana si el personaje colisiona con una banana
                if [banana for banana in self.bananas if self.migo.x < banana.banana_rect.x + banana.banana_rect.width and
                            self.migo.x + self.migo.width > banana.banana_rect.x and
                            self.migo.y < banana.banana_rect.y + banana.banana_rect.height and
                            self.migo.y + self.migo.height > banana.banana_rect.y]:
                    self.banana_sound.play()

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
            
                background_image = pygame.image.load("assets/images/background.png") # Cargar la imagen de fondo
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
                    self.problem.draw(screen) # Dibujar el problema
                else:
                    self.migo.draw(screen) # Dibujar el personaje
                    for banana in self.bananas:
                        banana.draw(screen) # Dibujar las bananas
                    for banana in self.bananas:
                        banana.update() # Actualizar la posicion de las bananas que estan cayendo
                pygame.display.update()
                pygame.time.Clock().tick(120) 

            # Reiniciar las variables del juego si el jugador gana o pierde
            self.game_time = 0
            self.problem_time = 0
            self.problem_visible = True
            self.problem_generated = False
            self.bananas = []
            self.bananas_gotten = []
            self.level += 1
            self.migo.x = self.screen_width // 2
            if self.win:
                # Mostrar pantalla de ganaste y aumentar el nivel que a su vez aumenta la velocidad de caida de las bananas
                self.win = False
                espera = 6
                self.win_sound.play()
                flag2 = True
                flag = True
                while espera > 0:
                    background_image = pygame.image.load("assets/images/background.png").convert()
                    original_width, original_height = background_image.get_size()
                    aspect_ratio = original_width / original_height
                    new_height = self.screen_height
                    new_width = int(new_height * aspect_ratio)
                    background_image = pygame.transform.scale(background_image, (new_width, new_height))
                    x = (self.screen_width - new_width) // 2
                    y = (self.screen_height - new_height) // 2
                    screen.fill((0, 0, 0)) 
                    screen.blit(background_image, (x, y))
                    textx = self.win_text.get_width()
                    screen.blit(self.win_text, ((self.screen_width - textx)//2, self.screen_height//2))
                    pygame.display.update()
                    espera -= self.clock.tick() / 1000
                    pygame.time.Clock().tick(250)
            else:
                # Mostrar pantalla de perdiste
                self.lose = False
                espera = 6
                self.lose_sound.play()
                while espera > 0:
                    background_image = pygame.image.load("assets/images/background.png")
                    original_width, original_height = background_image.get_size()
                    aspect_ratio = original_width / original_height
                    new_height = self.screen_height
                    new_width = int(new_height * aspect_ratio)
                    background_image = pygame.transform.scale(background_image, (new_width, new_height))
                    x = (self.screen_width - new_width) // 2
                    y = (self.screen_height - new_height) // 2
                    screen.fill((0, 0, 0)) 
                    screen.blit(background_image, (x, y))
                    textx = self.lose_text.get_width()
                    screen.blit(self.lose_text, ((self.screen_width- textx) //2, self.screen_height//2))
                    pygame.display.update()
                    espera -= self.clock.tick() / 1000
                    pygame.time.Clock().tick(250)
                return # Se retorna al menu principal
