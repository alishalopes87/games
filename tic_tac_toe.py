def build_board():
	game = []

	game.append(['A','B','C'])
	for row in range(1,4):
		row = []
		for column in range(1,4):
			column = "-"
			row.append(column)
		game.append(row)
	return game

def format_board(board):
	count = 0
	for row in board:
		if row == 0:
			print("|".join(row))
		else:
			print(count,"|".join(row))
		count+= 1

def is_winner(board,position,player):
	row = int(position[0])
	column = int(position[1])

	count = 0
	#check rows for three in a row
	for i in range(len(board[row])):
		if board[row][i] == player:
			count += 1
		if count >= 3:
			return True

	count = 0
	#check columns for three in a row
	for i in range(len(board)):
		if board[i][column] == player:
			count += 1
		if count >= 3:
			return True


	#check diagonals for three in a row
	if board[1][0] == player and board[1][0] == board[2][1] == board[3][2]: 
		return True
	elif board[1][2] == player and board[1][2] == board[2][1] == board[3][0]:
		return True






def make_move(board,position,player):

	row = int(position[0])
	column = int(position[1])

	if board[row][column] == '-':
		board[row][column] = player
	else:
		print()
		print('Invalid Move, try again')
		print()

	return board


def play_game(board=None):

	if not board:
		board = build_board()

	column_to_grid = {'A':0, 'B': 1, "C":2}
	player = input("Choose a player: X or Y ").upper()
	print()
	print("Player {}'s move".format(player))
	print()
	format_board(board)
	print()
	row = input("Choose row: 1, 2, or 3 ").upper()
	print()
	column = input("Choose column: A, B, or C ").upper()
	print()
	if column in column_to_grid:
		position = str(row), str(column_to_grid[column])
	else:
		print("Invalid selection")

	board = make_move(board,position,player)
	if is_winner(board,position,player):
		print("{} is the winner!!".format(player))
		print()
		play_again = input("Would you like to play again? Y or N ")
		print()
		if play_again.upper() == 'Y':
			play_game()
		else:
			return
	else:
		format_board(board)
		play_game(board)

play_game()









