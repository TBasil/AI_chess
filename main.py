import pygame
from board import Board
from ai import AI

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    clock = pygame.time.Clock()

    board = Board()
    ai = AI(board)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            board.handle_event(event)

        # Make AI move if it's AI's turn
        if board.turn == "black":
            ai.make_move()

        # Draw everything
        screen.fill((255, 255, 255))
        board.draw_board(screen)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
