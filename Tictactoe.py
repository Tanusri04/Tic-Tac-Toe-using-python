def Rules(): 
    print('''Hello, Welcome to the game of tic-tac-toe! 
The rules of the game are explained below with the help of an example.
This is how the board will look like and say you want to play 0 here,
------------
|   | 0 |   |
------------
|   |   |   |
------------
|   |   |   |
------------

it is the 1st row 2nd column so you have to type 1 2

Similarly, if you want to play X here,

------------
|   |   |   |
------------
|   |   | X |
------------
|   |   |   |
------------
 
it is the 2nd row 3rd column so you have to type 2 3

Hope you understood and Have fun''') 
def winner(game):#This function has all possible combinations by which a player can win 
    row1=game[0]
    row2=game[1]
    row3=game[2]
    if row1[0]==row1[1] and row1[0]==row1[2]: #checking for row 1
        if row1[0]==1:
            return "Player 1 wins"
        elif row1[0]==2:
            return "Player 2 wins"
    if row2[0]==row2[1] and row2[0]==row2[2]: #checking for row 2
        if row2[0]==1:
            return "Player 1 wins"
        elif row2[0]==2:
            return "Player 2 wins"
    if row3[0]==row3[1] and row3[0]==row3[2]: #checking for row3
        if row3[0]==1:
            return "Player 1 wins"
        elif row3[0]==2:
            return "Player 2 wins"
    if row1[0]==row2[0] and row1[0]==row3[0]: #checking for col1
        if row1[0]==1:   
            return "Player 1 wins"
        elif row1[0]==2:
            return "Player 2 wins"
    if row1[1]==row2[1] and row1[1]==row3[1]: #checking for col2
        if row1[1]==1:
            return "Player 1 wins"
        elif row1[1]==2:
           return "Player 2 wins"
    if row1[2]==row2[2] and row1[2]==row3[2]: #checking for col3
        if row1[2]==1:
            return "Player 1 wins"
        elif row1[2]==2:
           return "Player 2 wins"
    if row1[0]==row2[1] and row1[0]==row3[2]: #checks diagonal
        if row1[0]==1:
            return "Player 1 wins"
        elif  row1[0]==2:         
            return "Player 2 wins"
    if row1[2]==row2[1] and row1[2]==row3[0]: #checks second diagonal
        if row1[2]==1:
            return "Player 1 wins"
        elif row1[2]==2:
            return "Player 2 wins"
    elif 0 not in row1 and 0 not in row2 and 0 not in row3:
        return "It's a draw!"
    else:
         return None
def MakeBoard(board): #drawing the board
    gameboard=[[],[],[]] #gameboard is a list of list
    k=0
    for i in board:
        for j in i:
            if j==0:
                gameboard[k].append(' ')
            elif j==1:
                gameboard[k].append('0')
            elif j==2:
                gameboard[k].append('X')
        k+=1
    count=0
    print('\n \n')
    while count<3:
        print("----"*3)
        print('| {} | {} | {} |'.format(gameboard[count][0], gameboard[count][1], gameboard[count][2]))
        count+=1
    print("----"*3)  
def Player1(): 
	player1Turn = input("\n Player 1, its your turn ").strip().split()
	intList = []
	for elem in player1Turn:
		intList.append(int(elem) - 1) 
	return intList
def Player2(): 
	player2Turn = input("\nPlayer 2, its your turn ").strip().split()
	intList = []
	for elem in player2Turn:
		intList.append(int(elem) - 1)
	return intList

def player1Turn(): 
	user1Turn = Player1()
	if board[user1Turn[0]][user1Turn[1]] == 0:
		board[user1Turn[0]][user1Turn[1]] = 1
		return False
	else:
		return True

def player2Turn():
	user2Turn = Player2()
	if board[user2Turn[0]][user2Turn[1]] == 0:
		board[user2Turn[0]][user2Turn[1]] = 2
		return False
	else:
		return True
board = [[0, 0, 0], 
		 [0, 0, 0],
		 [0, 0, 0]]
def main():
	Rules()	
	nowinneryet=True
	while nowinneryet: 
		if nowinneryet == True: 
			turn = True
			while turn:
				MakeBoard(board)
				turn = player1Turn()
		if winner(board) != None and nowinneryet == True: 
			MakeBoard(board)
			print("\n")
			print(winner(board))
			nowinneryet = False
		if nowinneryet == True:	
			turn = True
			while turn:
				MakeBoard(board)	
				turn = player2Turn()
		if winner(board) != None and nowinneryet == True: 
			MakeBoard(board)
			print("\n")
			print(winner(board))
			nowinneryet = False
		
	
if __name__ == "__main__": main()
