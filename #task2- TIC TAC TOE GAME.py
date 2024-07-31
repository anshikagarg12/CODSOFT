import math
#step1 make the board
board = [' ' for _ in range(9)]

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6]+" | " + board[7] + " | " + board[8])
    


#to check for winner in game(row/column/diagonals align)
def check_win(board,player):
    win_cond = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8], [0,4,8],[2, 4, 6]         
    ]
    
    for condition in win_cond:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
    

#to check if board is filled completely
def check_full(board):
    return ' 'not in board

#function for player move

def player_move(board):
    while True:
        try: 
            move = int(input("Enter your move (0-8): ")) 
            if board[move] == ' ':
                board[move] = "X"
                break 
            else:
                print("Place is filled")
        except (IndexError , ValueError):
            print("Invalid move, please retry")


#minimax function to implement minimax algo
def minimax(board,depth, is_max):
    if check_win(board,'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_full(board):
        return 0
    
    if is_max:
        best_score = -math.inf
        for i in range(0,8):
            if board[i]==' ':
                board[i] = 'O'
                score = minimax(board,depth+1,False)
                board[i]=' '
                best_score = max(score,best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(0,8):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board,depth+1,True)
                board[i] = ' '
                best_score = min(score,best_score)
        return best_score

#function for computer's move
def comp_move(board):
    best_score = -math.inf
    move=0
    for i in range(0,8):
        if board[i] == ' ':
            board[i] = 'O'
            score =  minimax(board,0,False)
            board[i]=' '
            if score>best_score:
                best_score=score
                move = i
    board[move]='O'

def main():
    print("Let's play TIC TAC TOE")
    print_board(board)

    while True:
        player_move(board)
        if check_win(board,'X'):
            print_board(board)
            print("You win!")
            break

        if check_full(board):
            print_board(board)
            print("It's a Draw!")
            break

        comp_move(board)
        if check_win(board,'O'):
            print_board(board)
            print("Computer wins, Well played!")
            break
        if check_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)

if __name__ == "__main__" :
    main()