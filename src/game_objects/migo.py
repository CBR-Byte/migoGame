import pygame

class Migo:
    def __init__(self, x, y):
        self.x = x // 2
        self.y = y - 280
        self.width = 100
        self.height = 150
        self.velocity = 25
        self.frame = 0
        self.sprites = ["assets/character_sprites/walking_1.png","assets/character_sprites/walking_2.png",
           "assets/character_sprites/walking_3.png","assets/character_sprites/walking_4.png",
            "assets/character_sprites/walking_3.png","assets/character_sprites/walking_2.png", 
            "assets/character_sprites/walking_1.png","assets/character_sprites/walking_5.png",
            "assets/character_sprites/walking_6.png","assets/character_sprites/walking_7.png",
            "assets/character_sprites/walking_6.png","assets/character_sprites/walking_5.png",
            "assets/character_sprites/walking_1.png"]
        self.character = pygame.image.load(self.sprites[self.frame])
        self.character = pygame.transform.scale(self.character, (self.width, self.height))
        self.direction = 1
        self.last_direction = 1
        self.frame_duration = 0.1 
        self.last_frame_time = 0 

    def move(self, dx):
        current_time = pygame.time.get_ticks() / 1000.0  # Tiempo actual en segundos
        time_since_last_frame = current_time - self.last_frame_time

        if time_since_last_frame >= self.frame_duration:
            self.last_frame_time = current_time
            self.frame = (self.frame + 1) % len(self.sprites)
            self.character = pygame.image.load(self.sprites[self.frame])
            self.character = pygame.transform.scale(self.character, (self.width, self.height))

        if dx == 0:
            self.frame = 0
            self.character = pygame.image.load(self.sprites[self.frame])
            self.character = pygame.transform.scale(self.character, (self.width, self.height))
            if self.last_direction == -1:
                self.character = pygame.transform.flip(self.character, True, False)
        if dx == 1:
            self.x += self.velocity * dx
            self.last_direction = dx
        if dx == -1:
            self.x += self.velocity * dx
            self.last_direction = dx
            self.character = pygame.transform.flip(self.character, True, False)



    def draw(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        posicion_x = max(0, min(screen_width - self.width, self.x))

        screen.blit(self.character, (self.x, self.y))
