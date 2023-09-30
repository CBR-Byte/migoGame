import pygame

class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu_font = pygame.font.Font(None, 36)  # Choose a suitable font
        

    def draw(self, screen):
        background_image = pygame.image.load("assets/background.png")
        title_image = pygame.image.load("assets/title.png")
        title_image = pygame.transform.scale(title_image, (300, 100))
        play_image = pygame.image.load("assets/play.png")
        play_image = pygame.transform.scale(play_image, (100, 100))

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
        title_y = new_height // 3
        play_x = (self.screen_width - play_image.get_width()) // 2
        play_y = new_height // 2.3

        screen.fill((0, 0, 0))  # Establecer el color de fondo
        screen.blit(background_image, (x, y))
        screen.blit(title_image, (title_x, title_y))
        self.play_rect = screen.blit(play_image, (play_x, play_y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_rect.collidepoint(event.pos):
                    return "play"  # Signal to transition to the game

        return None
