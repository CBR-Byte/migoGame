import pygame

class Migo:
    def __init__(self, x, y):
        # Inicializar el personaje
        self.screen_width = x
        self.width = x * 0.05208333333
        self.height = y * 0.13888888888
        self.x = x // 2
        self.y = y - self.height*1.87
        self.velocity = 25
        self.frame = 0
        self.sprites = ["assets/images/character_sprites/walking_1.png","assets/images/character_sprites/walking_2.png",
           "assets/images/character_sprites/walking_3.png","assets/images/character_sprites/walking_4.png",
            "assets/images/character_sprites/walking_3.png","assets/images/character_sprites/walking_2.png", 
            "assets/images/character_sprites/walking_1.png","assets/images/character_sprites/walking_5.png",
            "assets/images/character_sprites/walking_6.png","assets/images/character_sprites/walking_7.png",
            "assets/images/character_sprites/walking_6.png","assets/images/character_sprites/walking_5.png",
            "assets/images/character_sprites/walking_1.png"]
        self.character = pygame.image.load(self.sprites[self.frame]).convert()
        self.character = pygame.transform.scale(self.character, (self.width, self.height))
        self.direction = 1
        self.last_direction = 1
        self.frame_duration = 0.1 
        self.last_frame_time = 0 

    def move(self, dx):
        current_time = pygame.time.get_ticks() / 1000.0  # Tiempo actual en segundos
        time_since_last_frame = current_time - self.last_frame_time

        if time_since_last_frame >= self.frame_duration: # Si ha pasado el tiempo suficiente para cambiar de frame
            self.last_frame_time = current_time
            self.frame = (self.frame + 1) % len(self.sprites) # Cambiar de frame
            self.character = pygame.image.load(self.sprites[self.frame]) # Cargar el nuevo frame
            self.character = pygame.transform.scale(self.character, (self.width, self.height)) # Escalar el frame

        if dx == 0:
            # Si no se esta moviendo, se muestra el primer frame
            self.frame = 0
            self.character = pygame.image.load(self.sprites[self.frame])
            self.character = pygame.transform.scale(self.character, (self.width, self.height))
            if self.last_direction == -1: # Si el ultimo movimiento fue hacia la izquierda, se voltea el sprite
                self.character = pygame.transform.flip(self.character, True, False)
        if dx == 1:
            # Si se va a salir de la pantalla, no se mueve
            if not  self.x + self.velocity > self.screen_width*0.72916666666:
                # Si se esta moviendo a la derecha, se mueve la posicion del personaje y se guarda la direccion
                self.x += self.velocity * dx
                self.last_direction = dx
        if dx == -1:
            # Si se va a salir de la pantalla, no se mueve
            if not self.x + self.velocity < self.screen_width*0.26041666666:
                # Si se esta moviendo a la izquierda, se mueve la posicion del personaje y se guarda la direccion
                self.x += self.velocity * dx
                self.last_direction = dx
                self.character = pygame.transform.flip(self.character, True, False)



    def draw(self, screen):
        # Dibujar el personaje en la pantalla
        screen.blit(self.character, (self.x, self.y))
