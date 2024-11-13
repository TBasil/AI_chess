import pygame
from board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption('Chess Game')
    clock = pygame.time.Clock()

    board = Board()

    running = True
    while running:
        screen.fill((0, 0, 0))  # Fill screen with black
        board.draw(screen)  # Draw the chessboard

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // 80, x // 80
                board.handle_click(row, col)  # Handle clicks on the chessboard

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Set the FPS

    pygame.quit()

if __name__ == "__main__":
    main()
