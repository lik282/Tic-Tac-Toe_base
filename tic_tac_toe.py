from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    while is_game_running:
        display_board(board)
    
    game_mode = get_menu_option()  # Get the game mode
    board = get_empty_board()  # Create an empty board
    current_player = 'X'  # Start with player 'X'
    is_game_running = True  # Flag to control the game loop
    
    while is_game_running:
        display_board(board)  # Display the current state of the board
        
        # Select coordinates based on game mode and current player
        if current_player == 'X':  # Player X is always human
            if game_mode == HUMAN_VS_HUMAN:
                x, y = get_human_coordinates(board, current_player)
            elif game_mode == HUMAN_VS_RANDOM_AI:
                x, y = get_human_coordinates(board, current_player)
            elif game_mode == HUMAN_VS_UNBEATABLE_AI:
                x, y = get_human_coordinates(board, current_player)
        elif current_player == 'O':  # Player O is AI
            if game_mode == RANDOM_AI_VS_RANDOM_AI or game_mode == HUMAN_VS_RANDOM_AI:
                x, y = get_random_ai_coordinates(board, current_player)
            elif game_mode == HUMAN_VS_UNBEATABLE_AI:
                x, y = get_unbeatable_ai_coordinates(board, current_player)
        
        # Make the move on the board
        board[x][y] = current_player
        
        
        # Check for winning or tie
        
        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)
        
        ### TO DO ###
        # in each new iteration of the while loop the program should 
        # alternate the value of `current_player` from `X` to `O`
        current_player = 'X'
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates
        x, y = get_human_coordinates(board, current_player)
        
        board[x][y] = current_player
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)


if __name__ == "__main__":
    main()