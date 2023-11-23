import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, "O"):
        return 10 - depth
    elif check_winner(board, "X"):
        return depth - 10
    elif is_full(board):
        return 0

    empty_cells = get_empty_cells(board)
    if maximizing_player:
        max_eval = -math.inf
        for row, col in empty_cells:
            board[row][col] = "O"
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for row, col in empty_cells:
            board[row][col] = "X"
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    empty_cells = get_empty_cells(board)
    alpha = -math.inf
    beta = math.inf

    for row, col in empty_cells:
        board[row][col] = "O"
        eval = minimax(board, 0, alpha, beta, False)
        board[row][col] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
        alpha = max(alpha, eval)
    
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row [0-2] column [0-2]): ").split())
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)
        
        if check_winner(board, "X"):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

play_game()
