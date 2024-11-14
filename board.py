import pygame
from piece import Pawn, Rook, Knight, Bishop, Queen, King
import os

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.tile_size = 60
        self.piece_images = {}  # Store images for drawing pieces
        self.load_piece_images()
        self.initialize_pieces()
        self.turn = "white"  # White starts the game

    def load_piece_images(self):
        # Load the piece images
        pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        colors = ['white', 'black']
        for color in colors:
            for piece in pieces:
                image_key = f"{color}_{piece}"
                image_path = f"assets/{image_key}.png"
                try:
                    self.piece_images[image_key] = pygame.image.load(image_path)
                except pygame.error:
                    print(f"Error: Image '{image_key}.png' not found in assets folder.")

    def initialize_pieces(self):
        # Initialize white pieces
        self.board[0][0] = Rook('white')
        self.board[0][1] = Knight('white')
        self.board[0][2] = Bishop('white')
        self.board[0][3] = Queen('white')
        self.board[0][4] = King('white')
        self.board[0][5] = Bishop('white')
        self.board[0][6] = Knight('white')
        self.board[0][7] = Rook('white')
        for col in range(8):
            self.board[1][col] = Pawn('white')

        # Initialize black pieces
        self.board[7][0] = Rook('black')
        self.board[7][1] = Knight('black')
        self.board[7][2] = Bishop('black')
        self.board[7][3] = Queen('black')
        self.board[7][4] = King('black')
        self.board[7][5] = Bishop('black')
        self.board[7][6] = Knight('black')
        self.board[7][7] = Rook('black')
        for col in range(8):
            self.board[6][col] = Pawn('black')

    def draw_board(self, screen):
        # Draw the board and pieces
        colors = [pygame.Color(235, 235, 208), pygame.Color(119, 148, 85)]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                piece = self.board[row][col]
                if piece:
                    image_key = f"{piece.color}_{piece.__class__.__name__.lower()}"
                    screen.blit(self.piece_images.get(image_key), (col * self.tile_size, row * self.tile_size))

    def handle_event(self, event):
        # Handle user clicks and piece selection (To be implemented)
        pass

    def get_piece_at(self, row, col):
        return self.board[row][col]

    def set_piece_at(self, row, col, piece):
        self.board[row][col] = piece
