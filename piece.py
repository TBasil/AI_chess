import pygame

class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
        self.image = pygame.image.load(f'assets/{color}_{piece_type}.png')
        self.image = pygame.transform.scale(self.image, (80, 80))

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def get_possible_moves(self, row, col, board):
        pass

    def filter_valid_moves(self, moves, board):
        valid_moves = [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
        return valid_moves

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'knight')

    def get_possible_moves(self, row, col, board):
        moves = [
            (row + 3, col + 1), (row + 3, col - 1), (row - 3, col + 1), (row - 3, col - 1),
            (row + 1, col + 3), (row + 1, col - 3), (row - 1, col + 3), (row - 1, col - 3),
            (row + 2, col + 2), (row + 2, col - 2), (row - 2, col + 2), (row - 2, col - 2)
        ]
        return self.filter_valid_moves(moves, board)

class King(Piece):
    def __init__(self, color):
        super().__init__(color, 'king')

    def get_possible_moves(self, row, col, board):
        moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)
        ]
        return self.filter_valid_moves(moves, board)

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, 'pawn')

    def get_possible_moves(self, row, col, board):
        direction = 1 if self.color == 'white' else -1
        moves = [(row + direction, col)]
        if (self.color == 'white' and row == 1) or (self.color == 'black' and row == 6):
            moves.append((row + 2 * direction, col))

        capture_moves = [(row + direction, col + 1), (row + direction, col - 1)]
        capture_moves = self.filter_valid_moves(capture_moves, board)

        all_moves = moves + capture_moves
        return self.filter_valid_moves(all_moves, board)

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, 'rook')

    def get_possible_moves(self, row, col, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < 8 and 0 <= c < 8:
                    if board.board[r][c] is None:
                        moves.append((r, c))
                    elif board.board[r][c].color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break
        return self.filter_valid_moves(moves, board)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, 'queen')

    def get_possible_moves(self, row, col, board):
        moves = []
        for i in range(1, 8):
            moves.append((row + i, col))  # Move down
            moves.append((row - i, col))  # Move up
            moves.append((row, col + i))  # Move right
            moves.append((row, col - i))  # Move left
            moves.append((row + i, col + i))  # Move diagonally down-right
            moves.append((row - i, col - i))  # Move diagonally up-left
            moves.append((row + i, col - i))  # Move diagonally down-left
            moves.append((row - i, col + i))  # Move diagonally up-right
        return self.filter_valid_moves(moves, board)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, 'bishop')

    def get_possible_moves(self, row, col, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            for i in range(1, 8):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < 8 and 0 <= c < 8:
                    if board.board[r][c] is None:
                        moves.append((r, c))
                    elif board.board[r][c].color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break
        return self.filter_valid_moves(moves, board)
