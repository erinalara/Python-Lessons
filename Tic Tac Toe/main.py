# Erina Lara

def print_board(board):     # prints board and places marker given user row/column selection
    for r in board:
        for c in r:
            if c == 0:
                print(" . ", end="")
            elif c == 1:
                print(" X ", end="")
            elif c == 2:
                print(" O ", end="")
            else:
                print(c, end='')
        print()

def is_valid(r, c, board):      # Determines if selected mark is valid 
    if (r != 1 and r != 2 and r!= 3) or (c != 1 and c != 2 and c!= 3): # Validates if out of bounds
        return False   
    if board[r][c] == 0:
        return True
    return False

def is_winner(board):   # Determines if a player has won after making a move
    for i in range(len(board)):
        if (board[i][1] == board[i][2] == board[i][3] and board[i][1] != 0) or (board[1][i] == board[2][i] == board[3][i] and board[1][i] != 0):
            return True
        if (board[1][1] == board[2][2] == board [3][3] or board[1][3] == board[2][2] == board [3][1]) and board[2][2] != 0:
            return True
    return False
        
def switch_player(current):
  print()



def main():     # Main function
    board = [[ '- ' , ' 0 ' , ' 1 ' , ' 2 ' ],
             ["0 ",0, 0, 0], 
             ["1 ",0, 0, 0], 
             ["2 ",0, 0, 0]]     # Board
    current = 1     # Sets current player
    win = 0         # Sets game to no wins

  
    for i in range(9):
        print_board(board)
                
        if is_winner(board) == True:    # Checks board if there is a winner
            if current == 2:    # Switches to winning player
                current = 1
            elif current == 1:
                current = 2
            print("Player",current, "wins!")    # Prints winning player
            win = 1     # Player has won, ending game
            break
       
        if current == 1:        # Prints X or O depending on player to differentiate mark
            print("X's turn")
        elif current == 2:
            print("O's turn")    
       
        r = (int(input("Give Row! "))) + 1      # Adds one to user input to give the correct mark
        c = (int(input("Give Column! "))) + 1
        while not is_valid(r, c, board):        # Loops until player makes valid choice
            r = (int(input("Give Row! "))) + 1
            c = (int(input("Give Column! "))) + 1
        print(r,c)
        board[r][c] = current   # Switches player after they make hteir move
        if current == 1:
            current = 2
        else:
            current = 1
        
    print_board(board)      # Prints board when no more moves can be played
    if win != 1 and is_winner(board) == True:   # Checks if last move is a winning move
        if current == 2:
            current = 1
        elif current == 1:
            current = 2
        print("Player",current, "wins!")
        
    elif win == 0:      # Game is a draw
        print("Game is a draw.")

main()