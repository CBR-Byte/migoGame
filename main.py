import pygame
from src.menu import MainMenu
from src.game import Game  

# Se inicializa pygame
pygame.init()

# Se definen las dimensiones de la pantalla para que sea dinamica
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
WIN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Migo")

def main(): # Funcion principal que ejecuta el juego
    menu = MainMenu(screen_width, screen_height) # Se crea el menu
    game = None # Se inicializa el juego en None para que no se ejecute hasta que se presione el boton de play

    while True: # Loop principal
        if game is None: # Si el juego es None, se ejecuta el menu
            menu.draw(WIN) # Se dibuja el menu
            pygame.display.update() # Se actualiza la pantalla
            action = menu.handle_events() # Se obtiene la accion del menu
            if action == "play": # Si la accion es play, se crea el juego
                game = Game(screen_width, screen_height) # Se crea el juego
        else: # Si el juego no es None, se ejecuta el juego
            game.run(WIN) # Se ejecuta el juego
            game = None # Se reinicia el juego

if __name__ == "__main__": # Se ejecuta la funcion principal
    main()