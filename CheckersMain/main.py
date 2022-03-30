import pygame
from Checkers.constants import WIDTH, HEIGTH, SQ_SIZE, RED
from Checkers.board import Board
from Checkers.game import Game


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQ_SIZE
    col = x // SQ_SIZE
    return row,col



def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game(WIN)



    while run:
        clock.tick(FPS)
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)
        
        
        game.update()

    pygame.quit()


main()
    