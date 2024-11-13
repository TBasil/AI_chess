import pygame

from piece import Piece, Knight, King, Pawn, Rook, Queen, Bishop

class Board:
    def __init__(self):
        self.grid_size = 8
        self.tile_size = 80
        self.board = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.selected_piece = None
        self.selected_piece_position = None
        self.possible_moves = []
        self.setup_pieces()

    def setup_pieces(self):
        # Place pawns in their starting positions
        for col in range(self.grid_size):
            self.board[1][col] = Pawn('black')
            self.board[6][col] = Pawn('white')

        # Place other pieces for black and white
        self.board[0][0] = Rook('black')
        self.board[0][1] = Knight('black')
        self.board[0][2] = Bishop('black')
        self.board[0][3] = Queen('black')
        self.board[0][4] = King('black')
        self.board[0][5] = Bishop('black')
        self.board[0][6] = Knight('black')
        self.board[0][7] = Rook('black')

        self.board[7][0] = Rook('white')
        self.board[7][1] = Knight('white')
        self.board[7][2] = Bishop('white')
        self.board[7][3] = Queen('white')
        self.board[7][4] = King('white')
        self.board[7][5] = Bishop('white')
        self.board[7][6] = Knight('white')
        self.board[7][7] = Rook('white')

    def draw(self, screen):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                piece = self.board[row][col]
                if piece:
                    piece.draw(screen, col * self.tile_size, row * self.tile_size)

    def handle_click(self, row, col):
        piece = self.board[row][col]
        if self.selected_piece is None:
            if piece:
                self.selected_piece = piece
                self.selected_piece_position = (row, col)
                self.possible_moves = piece.get_possible_moves(row, col, self)
        else:
            if (row, col) in self.possible_moves:
                self.move_piece(row, col)
            self.selected_piece = None
            self.possible_moves = []

    def move_piece(self, row, col):
        if self.selected_piece:
            start_row, start_col = self.selected_piece_position
            self.board[row][col] = self.selected_piece
            self.board[start_row][start_col] = None
            self.selected_piece = None
            self.possible_moves = []
