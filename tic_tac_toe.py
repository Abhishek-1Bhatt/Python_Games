from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[6]+"|"+board[7]+"|"+board[8])
def win_check(board,p1):
    if board[0]==board[1]==board[2]:
        if board[0]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[0]==board[3]==board[6]:
        if board[0]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[0]==board[4]==board[8]:
        if board[0]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[1]==board[4]==board[7]:
        if board[1]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[2]==board[5]==board[8]:
        if board[2]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[2]==board[5]==board[6]:
        if board[2]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[3]==board[4]==board[5]:
        if board[3]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif board[6]==board[7]==board[8]:
        if board[6]==p1:
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    else:
        return 'Next move'
board=["0","1","2","3","4","5","6","7","8"]
count=-1
p1=''
p2=''
while True:
    if count==-1:
        p1=input('Player 1 choose X or O')
        count+=1
        if p1=='X':
            p2='O'
        else:
            p2='X'
    elif count>=0 and count<=9:
        count+=1
        display_board(board)
        inp=int(input(f"Player 1's turn,{p1}"))
        board[inp]=p1
        display_board(board)
        if win_check(board, p1) == "Player 1 wins!":
            print("Player 1 wins!")
            break
        if count==9:
         print("It's a tie")
         break
        inp=int(input("Player 2's turn"))
        board[inp]=p2
        count+=1
        if win_check(board, p1) == "Player 2 wins!":
            print("Player 2 wins!")
            break
