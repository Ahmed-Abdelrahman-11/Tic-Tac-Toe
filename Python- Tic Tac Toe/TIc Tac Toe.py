#Functions:


def display_board(board):
    '''
        Takes a board as a list and prints out representaion starting from index 1 at the bottom left
    '''
    print(*board[7:] , sep = '|')
    print('------')
    print(*board[4:7] , sep = '|')
    print('------')
    print(*board[1:4] , sep = '|')

    

def player_input():
    
    '''
        Asks user for a marker x or o and returns tuple (player1 marker,player2 marker)
    '''
    
    marker = 'wrong'
    while marker not in ['X','O']:
        marker = input('Player 1, please choose a marker: x or o : ').upper()
        if marker == 'X':
            print('Great, player1 is X and player2 is O')
            return ('X', 'O')
        elif marker == 'O':
            print('Great, player1 is O and player2 is X')
            return ('O', 'X')
        else:
            print('Sorry not a valid option.')



def place_marker(board, marker, position):
    '''
        Takes   1-board as list 
                2-marker unpacked from tuple player_input()
                3-position as int from player_choice()
        Places the marker at the position of the list 
    '''
    board[position] = marker




def win_check(board, mark):
    '''
        checks if 3 of the same marker exists in vertical, horizantal, or diagnol sequence 
        and return True if win is found and False if no win 
        will be used after every move to check for a win 
    '''
    
    win_conditions =[board[1:4],
                     board[4:7],
                     board[7:],
                     [board[1],board[4],board[7]],
                     [board[2],board[5],board[8]],
                     [board[3],board[6],board[9]],
                     [board[1],board[5],board[9]],
                     [board[3],board[5],board[7]]] 
        
    return [mark]*3 in win_conditions





from random import randint

def choose_first():
    '''
        returns a str to be used as initial value for var turn
        turn will also be used later in conjunction with if to determine turns   
    '''
    if randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def space_check(board, position):
    '''
        returns True if position(int from 1 to 9) is free and False otherwise 
        will be used inside the player_choice() function 
    '''
    return board[position] not in ['X','O']


def full_board_check(board):
    '''
      Checks if the board is full and returns a boolean value.
      True if full, False otherwise.  
      will be used after every move to check for a tie.
    '''
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True



def player_choice(board):
    '''
        asks for a player's next position
        1- checks if digit 
        2- checks if in range (1-9)
        3- checks if the position is free space_check(board, position)
        If all 3 conditions are true, then return the position to be used in place_marker(board, marker, position).
    '''
        
    while True:
        
        choice = input('Choose your next position: (1-9)')
        
        if not choice.isdigit() :
            print("Not a digit")
        elif int(choice) not in range(1,10):
            print('Not in range')
        elif not space_check(board, int(choice)) :
            print('position taken')
        else:
            break
            
    return int(choice)




def replay():

    '''
        ask user to play again y or n 
        returns True if yes and False if no
        will be used later as var game_on with while loop in the event of a tie or a win
    '''
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N ")[0].upper()
        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to type in Y or N.")
    
    return choice == 'Y'





#game logic:




print('Welcome to Tic Tac Toe!')

while True:
    
    board = ['-']*10
    P1_marker , P2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? (Y,N): ')
    game_on = play_game[0].upper() == 'Y'
    
    while game_on:
                
        if turn == 'Player 1':
        # Player1 Turn

            print( f'{turn} turn : {P1_marker}' )
            display_board(board)
            position = player_choice(board)
            place_marker(board, P1_marker , position)
            
            if win_check(board, P1_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board) :
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        
        
        
        else:
        # Player1 Turn
            
            print( f'{turn} turn : {P2_marker}' )
            display_board(board)
            position = player_choice(board)
            place_marker(board, P2_marker , position)
            
            if win_check(board, P2_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board) :
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1' 
    
    if not replay():
        break


