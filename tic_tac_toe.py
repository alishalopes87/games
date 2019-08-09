game = []

def build_board():

	game.append(['A','B','C'])
	for row in range(1,4):
		row = []
		for column in range(1,4):
			column = "-"
			row.append(column)
		game.append(row)
	return game
game = build_board()


def format_board(board):
	count = 0
	for row in game:
		if row == 0:
			print("|".join(row))
		else:
			print(count,"|".join(row))
		count+= 1

def is_winner(board,position,player):
	row = int(position[0])
	column = int(position[1])
	print(row, column)

	count = 0
	for i in range(len(board)):
		for j in range(len(board[row])):
			if board[i][j] == player:
				count += 1
		if count >= 3:
			return True


def make_move(board,position,player):

	row = int(position[0])
	column = int(position[1])

	if board[row][column] == '-':
		board[row][column] = player
	else:
		return 'Invalid Move'

	return board


def play_game(board):
	column_to_grid = {'A':0, 'B': 1, "C":2}
	player = input("Choose a player: X or Y ").upper()
	print(player)
	format_board(board)
	row = input("Choose row: 1, 2, or 3 ").upper()
	column = input("Choose column: A, B, or C ").upper()
	if column in column_to_grid:
		position = str(row), str(column_to_grid[column])
	else:
		print("Invalid selection")

	board = make_move(board,position,player)
	if is_winner(board,position,player):
		print("{} is the winner!!".format(player))
		return 
	else:
		format_board(board)
		play_game(board)

play_game(game)









