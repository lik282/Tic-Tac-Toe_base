def get_human_coordinates(board, current_player):
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  row_labels = {'A': 0, 'B': 1, 'C': 2}
  col_labels = {'1': 0, '2': 1, '3': 2}

  while True:
        user_input = input(f"Player {current_player}, enter your move (A1, B2) or 'quit': ").strip().upper()

        # Check if user wants to quit
        if user_input == "QUIT":
            print("Thanks for playing!")
            exit()

        # Validate the input format
        if len(user_input) != 2:
            print("Invalid format. Use format like A1, B2, etc.")
            continue

        row_char, col_char = user_input[0], user_input[1]

        if row_char not in row_labels or col_char not in col_labels:
            print("Invalid coordinates. Rows: A-C, Columns: 1-3.")
            continue

        row = row_labels[row_char]
        col = col_labels[col_char]

        # Check if the spot is taken
        if board[row][col] != '.':
            print("That spot is already taken. Try again.")
            continue

        return (row, col)


def get_random_ai_coordinates(board, current_player):
    """
    Should return a tuple of 2 numbers. 
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """
    free_spaces = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == '.':
                free_spaces.append((row, col))

    if not free_spaces:
        return None

    return random.choice(free_spaces)


def get_unbeatable_ai_coordinates(board, current_player):
    """
    Should return a tuple of 2 numbers. 
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    The chosen coordinate should always stop the other player from winning or
    maximize the current player's chances to win.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """
    best_score = float('-inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == '.':
                board[row][col] = current_player
                score = minimax(board, 0, False, current_player)
                board[row][col] = '.'
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move


def minimax(board, depth, is_maximizing, ai_player):
    opponent = 'O' if ai_player == 'X' else 'X'
    winner = get_winning_player(board)

    if winner == ai_player:
        return 1
    elif winner == opponent:
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '.':
                    board[row][col] = ai_player
                    score = minimax(board, depth + 1, False, ai_player)
                    board[row][col] = '.'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '.':
                    board[row][col] = opponent
                    score = minimax(board, depth + 1, True, ai_player)
                    board[row][col] = '.'
                    best_score = min(score, best_score)
        return best_score


def get_winning_player(board):
    """
    Checks if there's a winner and returns the winning player, 'X' or 'O'.
    If no winner, returns None.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '.':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '.':
        return board[0][2]

    return None


def is_board_full(board):
    """
    Returns True if the board is full, False otherwise.
    """
    for row in board:
        if '.' in row:
            return False
    return True

# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 