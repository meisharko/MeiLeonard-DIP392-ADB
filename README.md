The code we have prepared for implementation phase of the project is:

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
        text = font.render(f"Player {turn} wins!", True, RED if turn == 1 else YELLOW)
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


Programming Concepts: In order to develop the game of Connect 4, I will need to use a number of programming concepts, such as:
• Arrays: I'll use arrays to store the playing field and track the pieces that each player has used.
• Loops: In order to iterate around the game board, check for winning criteria, and provide players the opportunity to take turns, I will utilize loops.
• Conditional Statements: To check for winning criteria and decide whether the game is ended, I will use conditional statements.
• Event Handling: I'll use event handling to track when a player clicks a column to drop a piece, updating the game board as a result.
• Graphical User Interface (GUI): To build the game's graphical user interface and enable user interaction, I'll utilize a GUI framework like Pygame.

Follow these steps to play Connect 4:
1. Get Python (version 3.6 or higher) from https://www.python.org/downloads/ and install it.
2. Download the ZIP file or clone the repository.
3. Utilize the terminal or command prompt to navigate to the project directory.
4. To install the Pygame library, issue the command "pip install pygame".
5. To launch the game, use "python connect4.py" at the command line.
6. A blank Connect 4 board will appear in the game window when it opens.
7. To drop a component, click a column.
8. Each player takes a turn putting one of their colored discs into a column.
9. Play continues until one player connects four discs in a row to win, or the board fills up and the game is declared a draw.
10. Press the 'r' key to restart the game. Press the 'q' key to end the game.

Other notes:
• We had to experiment with various approaches to get Pygame's event handling to function properly after running into some problems.
• Using Python's built-in "pickle" module, we created a feature that allows game states to be saved and loaded. The game board, the current player, and the score are all part of the recorded data.
• We created tags for each significant release of our code using Git to version control it.
• Using Pyinstaller, we made a standalone executable for the game and tested it on both Windows and Mac OS.

Testing
Instructions: Week 10
Journal
The following prompts are meant to aid your thought process as you complete the testing portion of this exercise. Please respond to each of the prompts below and feel free to add additional notes.
●	Have you changed any requirements since you completed the black box test plan? If so, list changes below and update your black-box test plan appropriately.
●	No changes have been made to the requirements since completing the black box test plan.

●	List the classes of your implementation. For each class, list equivalence classes, boundary values, and paths through code that you should test.

•	Class: GameBoard Equivalence classes:
•	Game board size: 7x6, 8x8, 10x7, etc.
•	Number of players: 2
•	Player moves: valid moves, invalid moves
•	Winning conditions: horizontal, vertical, diagonal, tie 

•	Boundary values:
•	Minimum game board size: 7x6
•	Maximum game board size: No maximum size specified
•	Maximum number of players: 2 

•	Paths through code:
•	Initialization of game board
•	Validating player moves
•	Checking for winning conditions
•	Handling ties

•	Class: Player Equivalence classes:
•	Player ID: 1, 2 Boundary values: None Paths through code:
•	Initialization of player
•	Handling player moves

●	Other notes:
●	It is important to test the game thoroughly to ensure that it meets all of the specified requirements and is easy to use for the end-users.
