import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Juega con Migo")
running = True
background_image = pygame.image.load("assets/background.png")
bananas = []
sprites = ["assets/character_sprites/walking_1.png","assets/character_sprites/walking_2.png",
           "assets/character_sprites/walking_3.png","assets/character_sprites/walking_4.png",
            "assets/character_sprites/walking_3.png","assets/character_sprites/walking_2.png", 
            "assets/character_sprites/walking_1.png","assets/character_sprites/walking_5.png",
            "assets/character_sprites/walking_6.png","assets/character_sprites/walking_7.png",
            "assets/character_sprites/walking_6.png","assets/character_sprites/walking_5.png",
            "assets/character_sprites/walking_1.png"]

frame = 0
character = pygame.image.load(sprites[frame])
character = pygame.transform.scale(character, (100, 150))
banana_img = pygame.image.load("assets/banana.png")
banana_img = pygame.transform.scale(banana_img, (50, 50))
posicion_x = screen_width // 2
posicion_y = screen_height - 280
velocidad_movimiento = 20  # Aumenta la velocidad de movimiento
velocidad_animacion = 100  # Aumenta la velocidad de la animación
direccion = 0  # 0: derecha, 1: izquierda

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        direccion = 0
        posicion_x += velocidad_movimiento
        frame = (frame + 1) % len(sprites)
    elif keys[pygame.K_LEFT]:
        direccion = 1
        posicion_x -= velocidad_movimiento
        frame = (frame + 1) % len(sprites)
    else:
        frame = 0

    # Carga la imagen del personaje correspondiente al fotograma actual
    character = pygame.image.load(sprites[frame])
    character = pygame.transform.scale(character, (100, 150))

    # Invierte la imagen si se mueve hacia la izquierda
    if direccion == 1:
        character = pygame.transform.flip(character, True, False)

    # Restringe la posición del personaje para que no se salga de la pantalla
    posicion_x = max(0, min(screen_width - character.get_width(), posicion_x))

    # Genera bananas aleatorias
    if random.randint(0, 100) < 80:  # Ajusta este valor para controlar la frecuencia de generación de bananas
        banana = {
            'image': banana_img,
            'x': random.randint(450, screen_width - 450),  # Ajusta el rango de generación en el eje X
            'y': 0,
            'width': 50,
            'height': 50,
        }
        bananas.append(banana)

    # Actualiza la posición de las bananas (hacen que caigan)
    for banana in bananas:
        banana['y'] += 10  # Ajusta la velocidad de caída de las bananas

    # Detecta colisiones con las bananas
    bananas = [banana for banana in bananas if not (posicion_x < banana['x'] + banana['width'] and
               posicion_x + character.get_width() > banana['x'] and
               posicion_y < banana['y'] + banana['height'] and
               posicion_y + character.get_height() > banana['y'])]


    # Redimensiona la imagen de fondo y la posición del personaje
    original_width, original_height = background_image.get_size()
    aspect_ratio = original_width / original_height
    new_height = screen_height
    new_width = int(new_height * aspect_ratio)
    background_image = pygame.transform.scale(background_image, (new_width, new_height))
    x = (screen_width - new_width) // 2
    y = (screen_height - new_height) // 2

    # Borra la pantalla y dibuja el fondo, el personaje y las bananas
    screen.fill((0, 0, 0))
    screen.blit(background_image, (x, y))
    screen.blit(character, (posicion_x, posicion_y))
    for banana in bananas:
        screen.blit(banana['image'], (banana['x'], banana['y']))
    pygame.display.flip()
    clock.tick(velocidad_animacion)