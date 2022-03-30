import pygame
from .constants import *
from Checkers.piece import Piece


class Board:
    def __init__(self):
        # Var's - Board
        self.board = []
        self.black_left = self.white_left = 12
        self.black_king = self.white_kings = 0
        self.create_board()

    def draw_squares(self, window):
        # Draw sq to create board on screen #
        window.fill(GREY)
        for r in range(ROWS):
            for c in range(r % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, [r * SQ_SIZE, c * SQ_SIZE, SQ_SIZE, SQ_SIZE])


    def get_piece(self, row, col):
        return self.board[row][col]



    def move(self, piece, row, col):
        # Move pawns #
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings +=1
            else:
                self.black_king +=1




    def create_board(self):
        # Create a board for checkers # 
        # 8 x 8 #
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)




