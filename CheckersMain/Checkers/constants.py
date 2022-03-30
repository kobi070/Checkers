import pygame

HEIGTH, WIDTH = 800, 800
ROWS, COLS = 8, 8
SQ_SIZE = WIDTH//COLS

# Path 
PATH = "assets\crown.png"


# Basic Colors #
BLACK = (0 , 0 , 0 )
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load(PATH), (44, 24))

