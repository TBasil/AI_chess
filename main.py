import pygame
from board import Board
from ai import AI
from piece import Piece

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Custom Chess Game')
clock = pygame.time.Clock()

board = Board()
ai = AI(board, 'black')

turn = 'white'  # Start with white's turn

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // 80, x // 80  # Calculate row and column based on mouse position

            # Player's turn to select or move a piece
            if turn == 'white' and board.selected_piece:
                # Player selects or moves the piece
                board.move_piece(*board.selected_piece_position, row, col)
                turn = 'black'  # Switch turn to AI
                ai.get_move()  # Let the AI make a move after the player
                board.selected_piece = None
                board.possible_moves = []  # Clear the possible moves after a move
            elif turn == 'white':
                # Select a piece if clicked on one
                board.select_piece(row, col)

            # Check for AI's move (only if it's the AI's turn)
            if turn == 'black':
                ai.make_move()
                turn = 'white'  # Switch turn to player

    # Clear the screen and draw the updated board
    screen.fill((0, 0, 0))
    board.draw_board(screen)
    pygame.display.flip()

    # Ensure the game runs at 30 FPS
    clock.tick(30)

pygame.quit()
