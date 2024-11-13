import pygame
from piece import Piece, Knight, King, Pawn, Rook, Queen, Bishop  # Assuming these are the piece classes you have

class Board:
    def __init__(self):
        self.grid_size = 8
        self.tile_size = 80
        self.board = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.selected_piece = None
        self.selected_piece_position = None  # Track the position of the selected piece
        self.possible_moves = []

        # Load piece images (adjust path as needed)
        self.white_rook_img = pygame.image.load("assets/white_rook.png")
        self.black_rook_img = pygame.image.load("assets/black_rook.png")
        self.white_knight_img = pygame.image.load("assets/white_knight.png")
        self.black_knight_img = pygame.image.load("assets/black_knight.png")
        self.white_pawn_img = pygame.image.load("assets/white_pawn.png")
        self.black_pawn_img = pygame.image.load("assets/black_pawn.png")
        self.white_bishop_img = pygame.image.load("assets/white_bishop.png")
        self.black_bishop_img = pygame.image.load("assets/black_bishop.png")
        self.white_queen_img = pygame.image.load("assets/white_queen.png")
        self.black_queen_img = pygame.image.load("assets/black_queen.png")
        self.white_king_img = pygame.image.load("assets/white_king.png")
        self.black_king_img = pygame.image.load("assets/black_king.png")

        self.setup_pieces()

    def __getitem__(self, index):
        # Allow indexing like board[row, col]
        row, col = index
        return self.board[row][col]

    def setup_pieces(self):
        # Place pawns in their starting positions
        for col in range(self.grid_size):
            self.board[1][col] = Pawn('black')  # Place black pawns
            self.board[6][col] = Pawn('white')  # Place white pawns

        # Place other pieces for black and white
        self.board[0][0] = Rook('black')  # Black rooks
        self.board[0][1] = Knight('black')  # Black knights
        self.board[0][2] = Bishop('black')  # Black bishops
        self.board[0][3] = Queen('black')  # Black queen
        self.board[0][4] = King('black')  # Black king
        self.board[0][5] = Bishop('black')  # Black bishops
        self.board[0][6] = Knight('black')  # Black knights
        self.board[0][7] = Rook('black')  # Black rooks

        self.board[7][0] = Rook('white')  # White rooks
        self.board[7][1] = Knight('white')  # White knights
        self.board[7][2] = Bishop('white')  # White bishops
        self.board[7][3] = Queen('white')  # White queen
        self.board[7][4] = King('white')  # White king
        self.board[7][5] = Bishop('white')  # White bishops
        self.board[7][6] = Knight('white')  # White knights
        self.board[7][7] = Rook('white')  # White rooks

    def select_piece(self, row, col):
        piece = self.board[row][col]
        if piece:
            self.selected_piece = piece
            self.selected_piece_position = (row, col)  # Store position
            self.possible_moves = piece.get_possible_moves(row, col, self.board)
        else:
            self.selected_piece = None
            self.selected_piece_position = None  # Reset position if no piece is selected
            self.possible_moves = []

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        if piece and (end_row, end_col) in self.possible_moves:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            # After a move, deselect the piece and clear possible moves
            self.selected_piece = None
            self.selected_piece_position = None  # Reset position
            self.possible_moves = []

    def draw_board(self, screen):
        colors = [(173, 216, 230), (240, 248, 255)]  # Light blue and off-white
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))

                # Highlight possible moves in red
                if (row, col) in self.possible_moves:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))

                # Draw pieces
                piece = self.board[row][col]
                if piece:
                    piece.draw(screen, col * self.tile_size, row * self.tile_size)

    def get_piece_at(self, row, col):
        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            return self.board[row][col]
        return None
