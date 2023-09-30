import pygame
from menu import MainMenu
from game import Game  # Assuming your game logic is in a separate file

# Initialize Pygame
pygame.init()

# Constants for the window
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
WIN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite-Based Game")

def main():
    menu = MainMenu(screen_width, screen_height)
    game = None  # Initialize the game object

    while True:
        if game is None:
            menu.draw(WIN)
            pygame.display.update()
            action = menu.handle_events()
            if action == "play":
                game = Game(screen_width, screen_height)  # Create the game object
        else:
            game.run(WIN)  # Run the game

if __name__ == "__main__":
    main()
