import random

class AI:
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def get_move(self):
        all_possible_moves = self.generate_all_moves()
        if all_possible_moves:
            return random.choice(all_possible_moves)  # Basic random selection for simplicity
        return None

    def generate_all_moves(self):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row, col]  # Using the correct way to access the board
                if piece and piece.color == self.color:  # Ensure only AI's pieces are considered
                    possible_moves = piece.get_possible_moves(row, col, self.board)
                    for move in possible_moves:
                        moves.append(((row, col), move))
        return moves

    def make_move(self):
        move = self.get_move()  # Get all possible moves for the AI
        if move:
            start_pos, end_pos = move
            start_row, start_col = start_pos
            end_row, end_col = end_pos

            # Add error checking before attempting to move
            piece = self.board[start_row, start_col]
            if piece:  # Ensure there's a piece at the starting position
                print(f"AI moving {piece.__class__.__name__} from ({start_row}, {start_col}) to ({end_row}, {end_col})")
                self.board.move_piece(start_row, start_col, end_row, end_col)
            else:
                print(f"Error: No piece at ({start_row}, {start_col})")
        else:
            print("Error: No valid moves for AI")
