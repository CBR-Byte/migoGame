import pygame
import pygame.mixer # Importar pygame.mixer para reproducir sonidos

class MainMenu: # Clase que representa el menu principal
    def __init__(self, screen_width, screen_height): # Constructor de la clase
        pygame.mixer.init() # Inicializar pygame.mixer
        self.click_sound = pygame.mixer.Sound("assets/sounds/menu.ogg") # Cargar el sonido del menu
        self.screen_width = screen_width 
        self.screen_height = screen_height
        self.menu_font = pygame.font.Font('assets/font/Gamer.ttf', 36)

    def draw(self, screen): # Funcion que dibuja el menu
        background_image = pygame.image.load("assets/images/background.png")
        title_image = pygame.image.load("assets/images/title.png")
        title_image = pygame.transform.scale(title_image, (300, 100))
        play_image = pygame.image.load("assets/images/play.png")
        play_image = pygame.transform.scale(play_image, (100, 100))

        exit_image = pygame.image.load("assets/images/exit.png")
        exit_image = pygame.transform.scale(exit_image, (100, 100))

        # Escalar la imagen de fondo para que encaje en la pantalla
        original_width, original_height = background_image.get_size()
        aspect_ratio = original_width / original_height
        new_height = self.screen_height
        new_width = int(new_height * aspect_ratio)
        background_image = pygame.transform.scale(background_image, (new_width, new_height))

        # Calcular las posiciones centradas
        x = (self.screen_width - new_width) // 2
        y = (self.screen_height - new_height) // 2
        title_x = (self.screen_width - title_image.get_width()) // 2
        title_y = new_height // 2.5
        play_x = (self.screen_width - play_image.get_width()) // 2
        play_y = title_y + play_image.get_height() 
        exit_x = (self.screen_width - exit_image.get_width()) // 2
        exit_y = play_y + exit_image.get_height() + 20

        screen.fill((0, 0, 0))
        screen.blit(background_image, (x, y)) # Dibujar la imagen de fondo
        screen.blit(title_image, (title_x, title_y)) # Dibujar la imagen del titulo
        self.play_rect = screen.blit(play_image, (play_x, play_y)) # Dibujar la imagen del boton de play
        self.exit_rect = screen.blit(exit_image, (exit_x, exit_y)) # Dibujar la imagen del boton de exit


    def handle_events(self): # Funcion que maneja los eventos del menu
        for event in pygame.event.get(): # Loop que recorre los eventos
            if event.type == pygame.QUIT: # Si se presiona el boton de salir, se cierra el juego
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Si se presiona el boton del mouse se verifica si se presiono el boton de play o exit
                if self.play_rect.collidepoint(event.pos):
                    self.click_sound.play()
                    return "play" # Si se presiono el boton de play, se retorna play
                if self.exit_rect.collidepoint(event.pos):
                    self.click_sound.play() 
                    pygame.quit() # Si se presiono el boton de exit, se cierra el juego
                    quit()
        return None
