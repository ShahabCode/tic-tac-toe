from termcolor import colored

board = list(range(1, 10))
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
moves = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def make_move(board, player, move, undo=False):
    if can_move(board, move):
        board[move - 1] = player
        win = is_winner(board, player)
        if undo:
            board[move - 1] = move  
        return True, win
    return False, False


def can_move(board, move):
    if move in range(1, 10) and isinstance(board[move - 1], int):
        return True
    else:
        return False


def is_winner(board, player):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if board[j] != player:
                win = False
                break
        if win:
            break
    return win


def has_empty_space():
    return board.count("X") + board.count("O") != 9


def computer_move():
    move = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            move = i
            break

    if move == -1:
        for j in range(1, 10):
            if make_move(board, me, j, True)[1]:
                move = j
                break

    if move == -1:
        for tup in moves:
            for m in tup:
                if move == -1 and can_move(board, m):
                    move = m
                    break
                
    return make_move(board, computer, move)


me, computer = "X", "O"
print("\nPlayer: X\nComputer: O\n")

while has_empty_space():
    print_board()
    move = int(input("Choose your move (1-9): "))
    moved, won = make_move(board, me, move)
    if not moved:
        print(colored("Invalid number!\ntry again. . .", "yellow"))
        continue
    if won:
        print_board()
        print(colored("You won!", "green"))
        break
    elif computer_move()[1]:
        print_board()
        print(colored("You lose!", "red"))
        break

if not is_winner(board, me) and not is_winner(board, computer) and not has_empty_space():
    print(colored("It's a draw! Play again.", "yellow"))