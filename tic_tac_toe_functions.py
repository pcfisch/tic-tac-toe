def print_board(board=[['0','1','2'], ['3','4','5'], ['6','7','8']]):
    """Function to print a given game board for tic-tac-toe.

    Args:
        board (list, list): List of 3 lists depicting rows of game board.
                                Will fill the squares of the board with specified values.
                                Defaults to [['0','1','2'], ['3','4','5'], ['6','7','8']].

    Returns:
        board (list, list): Prints out string with board borders and squares of specified value.
                            Returns list of lists with specified square values.
    """
    
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}\n---|---|---\n "
          f"{board[1][0]} | {board[1][1]} | {board[1][2]}\n---|---|---\n"
          f" {board[2][0]} | {board[2][1]} | {board[2][2]}\n\n")
    
    return board

def player():
    """Asks player one of tic-tac-toe for input on which item they want to use for filling
       in the squares (i.e. 'x' or 'o'). Any other characters than 'x' and 'o' will not be
       allowed as input.

    Returns:
        player_1(str): Returns string according to item pick ('x' or'o').
        player_2(str): Returns the item string player one did not choose ('x' or 'o').
    """
    player_1 = input('Player 1 please choose item "x" or "o": ')
    
    while player_1 != "x" and player_1 != "o":
        player_1 = input("Invalid input. Please choose either the lowercase letter 'x' or the lowercase letter 'o'.\n")
    
    player_2 = "o" if player_1 == "x" else "x"
    print(f"Player 1 chose {player_1}, player 2 will use {player_2}\n")

    return player_1, player_2

def move(square_list=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
         move_board=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]):
    
    """Function asks players for input to make a move by picking a number between
       0 and 8 representing the squares of the tic-tac-toe board.

    Args:
        square_list (list,list): list of lists with square indices where inside
        lists contain [row,col] of square

        move_board (list, list): list with three lists depicting rows of game
        board with three columns.

    Returns:
        square (int): int between 0 and 8 according to input of player.
        depicts pick of square
        row_col (list): list with int depicting row and column of picked
        square according to square_list
        player (int): 1 or 2 depending on whose turn it is (player 1 or player 2)
    """

    x_count, o_count= 0, 0

    for i in range(9):
        if move_board[i] == 'x':
            x_count += 1
            o_count += 0
        elif move_board[i] == 'o':
            x_count += 0
            o_count += 1
        elif move_board[i] == ' ':
            x_count += 0
            o_count += 0

    if x_count == o_count:
        player = 1
    elif x_count != o_count:
        player = 2


    print(f"Player {player} make your move!")
    square = int(input("Please pick one of the squares (0 to 8) for your item\n\n"))
    
    row_col = square_list[square]
    return row_col, square, player



def check_double_square(row = 0, col = 0,
                        current_board=[[' ',' ',' '],
                                       [' ',' ',' '],
                                       [' ',' ',' ']]):

    if current_board[row][col] != ' ':
        print("This square has already been taken! Choose another square!\n")
        square_taken = True
    else:
        square_taken = False

    return square_taken



def board_update(current_board=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']],
                 current_player=1, row_col=[0, 0], player_1='x', player_2='o'):
    if current_player == 1:
        current_board[row_col[0]][row_col[1]] = player_1
    else:
        current_board[row_col[0]][row_col[1]] = player_2
    
    print_board(board=current_board)
    
    return current_board



def win_status(player_1='x', player_2='o',
               current_board=[['o','o','x'],
                              ['x','x','o'],
                              ['o','x','o']]):

    row_col_dia = list()
    for i in range(3):
        for j in range(3):
            row_col_dia.append(current_board[i][j])

    if row_col_dia[0:3] == ['x','x','x'] or row_col_dia[3:6] == ['x','x','x'] or row_col_dia[6:] == ['x','x','x']:
        game_end = True
        if player_1 == 'x':
            print('Game is over! Congratulations, Player 1, you won!')
        elif player_2 == 'x':
            print('Game is over! Congratulations, Player 2, you won!')
    elif row_col_dia[0:3] == ['o','o','o'] or row_col_dia[3:6] == ['o','o','o'] or row_col_dia[6:] == ['o','o','o']:
        game_end = True
        if player_1 == 'o':
            print('Game is over! Congratulations, Player 1, you won!')
        elif player_2 == 'o':
            print('Game is over! Congratulations, Player 2, you won!')
    elif row_col_dia[0:7:3] == ['x','x','x'] or row_col_dia[1:8:3] == ['x','x','x'] or row_col_dia[2:9:3] == ['x','x','x']:
        game_end = True
        if player_1 == 'x':
            print('Game is over! Congratulations, Player 1, you won!')
        elif player_2 == 'x':
            print('Game is over! Congratulations, Player 2, you won!')
    elif row_col_dia[0:7:3] == ['o','o','o'] or row_col_dia[1:8:3] == ['o','o','o'] or row_col_dia[2:9:3] == ['o','o','o']:
        game_end = True
        if player_1 == 'o':
            print('Game is over! Congratulations, Player 1, you won!')
        elif player_2 == 'o':
            print('Game is over! Congratulations, Player 2, you won!')
    elif row_col_dia[0:9:4] == ['x','x','x'] or row_col_dia[6:1:-2] == ['x','x','x']:
        game_end = True
        if player_1 == 'x':
            print('Game is over! Congratulations, Player 1, you won!')
        elif player_2 == 'x':
            print('Game is over! Congratulations, Player 2, you won!')
    elif row_col_dia[0:9:4] == ['o','o','o'] or row_col_dia[6:1:-2] == ['o','o','o']:
        game_end = True
        if player_1 == 'o':
            print('Game is over! Congratulations, Player 1, you won!')
        elif player_2 == 'o':
            print('Game is over! Congratulations, Player 2, you won!')
    elif ' ' not in row_col_dia:
        print("Game is over! It's a draw!")
        game_end = True
    else:
        game_end = False
        pass # Game is still going on

    return game_end