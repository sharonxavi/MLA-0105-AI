def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
7
def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for _ in range(9):  
        while True:
            try:
                row = int(input(f"Player {players[current_player]}, enter row (0-2): "))
                col = int(input(f"Player {players[current_player]}, enter column (0-2): "))
                if is_valid_move(board, row, col):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            return

        current_player = 1 - current_player 

    print("It's a draw!")

play_game()
