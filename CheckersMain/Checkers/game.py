import pygame
from .constants import BLACK, WHITE, SQ_SIZE, ROWS, COLS
from .board import Board


class Game:
    def __init__(self, win) :
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selcted = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}
    
    def select(self, row, col):
        if self.selcted:
            result = self._move(row,col)
            if not result:
                self.selcted = None
                self.select(row,col)
        else:
            piece = self.board.get_piece(row,col)
            if piece != 0 and piece.color == self.turn:
                self.select = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False


    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == WHITE or piece.king:
            moves.update(self._travarese_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._travarese_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == BLACK or piece.king:
                moves.update(self._travarese_left(row + 1, max(row + 3, 1), -1, piece.color, left))
                moves.update(self._travarese_right(row + 1, max(row + 3, 1), -1, piece.color, right))
        return moves
            

    def _travarese_left(self, start, stop, step, color,left ,skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board.get_piece(r, left)
            if current == 0:
                if skipped and not last:
                    break
                elif skip_only:
                    pass
                else:
                    moves[(r, left)] = last
                if last :
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)
            elif current.color == color:
                break
            else:
                last = [current]


            
            left -= 1

    def _travarese_right(self, start, stop, step ,color,right ,skipped=[]):
        pass

    def _move(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selcted and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selcted, row, col)
        else:
            return False
        return True

    def change_turen(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK


    def reset(self):
        self._init()

        