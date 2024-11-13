import random
from board import Board

def ai_move(board):
    possible_moves = []
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece and piece.color == 'black':  # Assume AI plays black
                moves = piece.get_possible_moves(row, col, board)
                for move in moves:
                    possible_moves.append((row, col, move))

    if possible_moves:
        move = random.choice(possible_moves)
        start_row, start_col, (end_row, end_col) = move
        board.move_piece(end_row, end_col)
