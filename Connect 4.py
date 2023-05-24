import pygame
import random

# Initialize pygame
pygame.init()

# Set the game window size and title
WINDOW_SIZE = (700, 600)
pygame.display.set_caption("Connect 4")
screen = pygame.display.set_mode(WINDOW_SIZE)

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set the board size
ROWS = 6
COLS = 7

# Set the size of each cell in the board
CELL_SIZE = 100

# Set the size of the gap between cells
GAP_SIZE = 10

# Define the board array
board = [[0] * COLS for _ in range(ROWS)]

# Define the turn variable
turn = 1

# Define a function to draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE + GAP_SIZE, row * CELL_SIZE + GAP_SIZE, CELL_SIZE, CELL_SIZE))
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * CELL_SIZE + CELL_SIZE/2 + GAP_SIZE), int(row * CELL_SIZE + CELL_SIZE/2 + GAP_SIZE)), int(CELL_SIZE/2 - GAP_SIZE))
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int(col * CELL_SIZE + CELL_SIZE/2 + GAP_SIZE), int(row * CELL_SIZE + CELL_SIZE/2 + GAP_SIZE)), int(CELL_SIZE/2 - GAP_SIZE))

# Define a function to drop a piece
def drop_piece(col):
    global turn
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = turn
            if turn == 1:
                turn = 2
            else:
                turn = 1
            return True
    return False

# Define a function to check for a win
def check_win():
    for col in range(COLS-3):
        for row in range(ROWS):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != 0:
                return True
    for col in range(COLS):
        for row in range(ROWS-3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != 0:
                return True
    for col in range(COLS-3):
        for row in range(ROWS-3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != 0:
                return True
    for col in range(COLS-3):
        for row in range(3, ROWS):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != 0:
                return True
    return False

# Define a function to get valid moves
def get_valid_moves():
    valid_moves = []
    for col in range(COLS):
        if board[0][col] == 0:
            valid_moves.append(col)
    return valid_moves

# Define an AI move function
def ai_move():
    valid_moves = get_valid_moves()
    return random.choice(valid_moves)

# Define the main game loop
def main_loop():
    running = True
    game_over = False

    # Intro message
    intro_font = pygame.font.Font(None, 48)
    intro_text = intro_font.render("Welcome to Connect 4!", True, RED)
    intro_text_rect = intro_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 50))

    # Start game button
    start_game_button = pygame.Rect(250, 300, 200, 50)
    start_game_text = intro_font.render("Start Game", True, BLACK)
    start_game_text_rect = start_game_text.get_rect(center=start_game_button.center)

    # Quit button
    quit_button = pygame.Rect(250, 380, 200, 50)
    quit_text = intro_font.render("Quit", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)

    # Loop until the user clicks the close button or starts the game
    while running and not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # Check if the start game button was clicked
                if start_game_button.collidepoint(event.pos):
                    game_over = True
                # Check if the quit button was clicked
                elif quit_button.collidepoint(event.pos):
                    running = False

        # Draw the intro screen
        screen.fill(BLACK)
        screen.blit(intro_text, intro_text_rect)
        pygame.draw.rect(screen, RED, start_game_button)
        screen.blit(start_game_text, start_game_text_rect)
        pygame.draw.rect(screen, RED, quit_button)
        screen.blit(quit_text, quit_text_rect)

        # Update the screen
        pygame.display.update()

    if game_over:
        # Call the game start function
        start_game()

    # Quit pygame
    pygame.quit()

# Function to start the game
def start_game():
    running = True
    game_over = False

    # Loop until the user clicks the close button or the game is over
    while running and not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                # Get the column where the user clicked
                col = event.pos[0] // CELL_SIZE
                if drop_piece(col):
                    if check_win():
                        print(f"Player {turn} wins!")
                        game_over = True
                    else:
                        draw_board()

        # AI's turn
        if turn == 2 and not game_over:
            ai_col = ai_move()
            if drop_piece(ai_col):
                if check_win():
                    print(f"Player {turn} wins!")
                    game_over = True
                else:
                    draw_board()

        # Update the screen
        pygame.display.update()

    # Game over message
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {turn} wins!", True, RED if turn == 2 else YELLOW)
        text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
        screen.blit(text, text_rect)

    # Keep the window open until the user closes it
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    # Quit pygame
    pygame.quit()

# Call the main game loop
main_loop()
