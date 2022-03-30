import pygame
from .constants import BLACK, CROWN, ROWS, WHITE, SQ_SIZE, COLS, GREY


class Piece:

    PADDING = 15
    BOARDER = 2


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False # Start case = False
        self.x = 0
        self.y = 0
        self.calc_position()

        self.direction = None  # Positive for white player and Negetive for black player



    



    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def delete(self, row, col):
        pass


    def calc_position(self):
        # Center the (x,y) in the sq's
        self.x = SQ_SIZE * self.col + SQ_SIZE // 2
        self.y = SQ_SIZE * self.row + SQ_SIZE // 2

    def make_king(self):
        self.king = True
    

    def draw(self, win):
        # Draw a piece
        radius = SQ_SIZE // 2 - self.PADDING 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.BOARDER )
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()// 2,self.y - CROWN.get_height() // 2))
    

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()


    def __repr__(self):
        return str(self.color)




    