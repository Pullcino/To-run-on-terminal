board = []

for i in range(3):

    line = []

    for j in range(3):

        line.append(' ')

    board.append(line)

def show_board():

    for line in board:

        print("|".join(line))

        print("-" * 5)

def verify_winner(player):

    for i in range(3):

        all_cells_lines = True
        all_cells_columns = True

        for j in range(3):

            if board[i][j] != player:

                all_cells_lines = False

            if board[j][i] != player:

                all_cells_columns = False

        if all_cells_lines or all_cells_columns:

            return True
        
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:

            return True
        
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:

            return True
        
        return False


def play_(player):

    while True:

        play = input(f"Player {player}, choose the line and column (example: 0 2): ")

        try:

            line, column = map(int, play.split())

            if board[line][column] == ' ':
                
                board[line][column] = player

                break

            else:

                print("Position occupied, please try again.: ")

        except:
            print("invalid entry, Try again: ")

actual_play = 'X'

for _ in range(9):

    show_board()

    play_(actual_play)

    if verify_winner(actual_play):

        show_board()

        print(f"Player {actual_play} win")

        break

    actual_play = 'O' if actual_play == 'X' else 'X'

else: 

    show_board()

    print("Draw")