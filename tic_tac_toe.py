from tic_tac_toe_functions import player, move, check_double_square, print_board, board_update, win_status

# Tic-tac-toe game
if __name__ == "__main__":

    another_game = 'yes'
    # while loop to ask if players want to go another round. if yes, start over again
    while another_game == 'yes':

        # 1. Start a new round of Tic-tac-toe, define and show board with numbers for squares
        print("\nHi players! Let's have fun and welcome to a new round of Tic-Tac-Toe!\n"
            "This is your board. When choosing where to put your item, please refer to the numbers given here:\n")
        
        square_nums =[['0','1','2'], ['3','4','5'], ['6','7','8']]
        print_board(board=square_nums)

        # 2. Players choose items
        player_1, player_2 = player()

        # 3.0 Define play board (empty)
        the_board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

        move_board = the_board[0]
        for i in range(1,3):
            for j in range(3):
                move_board.append(the_board[i][j])

        # while loop for iterating through again and again until somebody won or draw
        winner = False
        while winner == False:
   
            valid_move = 1
            while valid_move == 1:

                # Player whose turn it is make your move:
                row_col, square, cur_player = move(move_board=move_board)

                # Check if chosen square had already been taken in a move before:
                square_taken = check_double_square(row=row_col[0], col=row_col[1], current_board=the_board)
                
                if not square_taken:
                    valid_move = 0 
                else:
                    continue
            
            if cur_player == 1:
                move_board[square] = player_1
            elif cur_player == 2:
                move_board[square] = player_2

            # 4. Update the board and show current status of the board to the players
            the_board = board_update(current_board=the_board, current_player=cur_player, row_col=row_col,
                                    player_1=player_1, player_2=player_2)
            
           # print_board(board=the_board)

            # 5. Check winning/draw status
            winner = win_status(player_1=player_1, player_2=player_2, current_board=the_board)

            if winner == True:
                another_game = input('Do you want to play another game? yes/no: ')
            else:
                pass

            if another_game == 'no':
                break
            else:
                pass