

import math

# Create board
board = [" " for _ in range(9)]

# Display board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check winner
def check_winner(board):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Tie"

    return None


# Minimax Algorithm
def minimax(board, depth, is_maximizing):

    result = check_winner(board)

    if result == "O":
        return 1

    elif result == "X":
        return -1

    elif result == "Tie":
        return 0


    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score


    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# AI Move
def ai_move():

    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


# Main Game
print("Tic-Tac-Toe AI Game")
print("You are X and AI is O")

print_board()

while True:

    # Human move
    player = int(input("Enter position (1-9): ")) - 1

    if board[player] == " ":
        board[player] = "X"
    else:
        print("Position already taken!")
        continue

    print_board()

    if check_winner(board):
        break


    # AI move
    print("AI is thinking...")
    ai_move()

    print_board()

    if check_winner(board):
        break


winner = check_winner(board)

if winner == "Tie":
    print("Game Draw!")

else:
    print(winner + " wins!")
