# ConnectX game in Python

import pygame
import sys
import random

def connect4():
	# Color = (r,g,b)
	BLUE = (0, 0, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	YELLOW = (255, 255, 0)
	GREEN = (0, 255, 0)
	WHITE = (255, 255, 255)

	board_ROWS = 6
	board_COLUMNS = 7

	# define a function for the game board
	def createBoard(ROWS, COLUMNS):
		board = []
		# create a list that has 7 uniform elements in it (The uniform element here is 0)
		# each element of the list corresponds to one column in our board
		# create 5 more copies of that list and append all of them to our empty board list (including the original copy of the list)
		# each list inside the board list now corresponds to the board's row
		for rowCounter in range(board_ROWS):
			# list comprehension
			row = [0 for column in range(COLUMNS)]
			board.append(row)

		return board

	# define a function that will determine whether a specific column in our board still has an empty slot or not
	def isFree(board, column):
		return board[0][column] == 0

	# define a function that will return the best possible available slot in a specific column
	def getTheAvailableRow(board, column):
		# assess each slot (starting from the very bottom row of the board) if it can still accept a piece or not
		row = board_ROWS - 1
		for index in range(board_ROWS):
			if board[row][column] == 0:
				return row
			row = row - 1

	# define a function that will enable us to drop a piece in our game board
	def dropPiece(board, row, column, piece):
		# update the values inside the board
		board[row][column] = piece

	# define a function that will print the created game board
	def printBoard(board):
		rowLabels = [1, 2, 3, 4, 5, 6, 7]
		
		for label in rowLabels:
			print("", label, end=" ")
		print()

		for row in board:
			print(row)

	# define a function that will specify all the possible winning game scenarios
	def winningMove(board, piece):
		# Determine all possible locations where four same-colored pieces can be possibly connected
		# Horizontal Lines
		for column in range(board_COLUMNS-3):
			for row in range(board_ROWS):
				if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
					return True

		# Vertical Lines
			for column in range(board_COLUMNS):
				for row in range(3, board_ROWS):
					if board[row][column] == piece and board[row-1][column] == piece and board[row-2][column] == piece and board[row-3][column] == piece:
						return True

		# Positively-sloped Diagonals
			for column in range(board_COLUMNS-3):
				for row in range(3, board_ROWS):
					if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
						return True

		# Negatively-sloped Diagonals
			for column in range(board_COLUMNS-3):
				for row in range(board_ROWS-3):
					if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
						return True

	# define a function that will draw our game board on the pygame window
	def drawBoard(board):
		for column in range(board_COLUMNS):
			for row in range(board_ROWS):
				# rect (Surface, color, Rect, width=0)
				# rect (Surface, color, (x coordinate, y coordinate, widthOfTheRect, heightOfTheRect))
				pygame.draw.rect(screen, BLUE, (column*square_size, screenTopSpace + (row+1)*square_size, square_size, square_size))

				# circle (Surface, color, pos, radius, width=0)
				# circle (Surface, color, coordinates of the center, radius, width=0)
				pygame.draw.circle(screen, BLACK, (int((column*square_size)+(square_size/2)), screenTopSpace + int(((row+1)*square_size)+(square_size/2))), radiusOfPiece)

		# change the black circles on the game board into colored circles whenever 0 is replaced by either 1 or 2
		for column in range(board_COLUMNS):
			for row in range(board_ROWS):
				if board[row][column] == 1:
					pygame.draw.circle(screen, RED, (int((column*square_size)+(square_size/2)), screenTopSpace + int(((row+1)*square_size)+(square_size/2))), radiusOfPiece)

				elif board[row][column] == 2:
					pygame.draw.circle(screen, YELLOW, (int((column*square_size)+(square_size/2)), screenTopSpace + int(((row+1)*square_size)+(square_size/2))), radiusOfPiece)

		pygame.display.update()

	# define a function that will save the current state of the game to a file
	def saveState(board, player_turn, move):
		fileHandle = open("assets/saves/save_state_6x7.txt", "w")

		for row in board:
			fileHandle.write(str(row) + "\n")

		fileHandle.write(str(player_turn) + "\n")
		fileHandle.write(str(move) + "\n")
		fileHandle.close()

	# define a function that will load the last saved state of the game from a file
	def loadState():
		fileHandle = open("assets/saves/save_state_6x7.txt", "r")

		# assign an empty list that will store data collected from each line of a file
		list_board = []
		for line in fileHandle:
			list_board.append(line[0:-1])

		# remove the the last 2 elements of the list since and store each of them in the moves and turn variables
		moves = int(list_board.pop())
		turn = int(list_board.pop())
			
		# since all elements stored in the list_board list are in the form data-type strings we'll remove the '[', ']', ' ', and ',' characters in them so we can create a new list that does not contain strings
		for index in range(board_ROWS):
			list_board[index] = list_board[index][1:-1].replace(",", "")
			list_board[index] = list_board[index].replace(" ", "")

		# Now, create a list representation of our game board
		board = []
		for row in range(board_ROWS):
			temp_list = []
			for column in range(board_COLUMNS):
				temp_list.append(int(list_board[row][column]))
			board.append(temp_list)

		return board, turn, moves
	# end of defining functions

	# Call the createBoard function and print it
	game_board =  createBoard(board_ROWS, board_COLUMNS)
	printBoard(game_board)

	# start pygame
	pygame.init()

	square_size = 96
	screenTopSpace = 28

	# radius of circle in the definition function drawboard
	radiusOfPiece = int(square_size/2 - 5)

	# set the dimensions of our pygame screen/window
	screen_width = board_COLUMNS*square_size
	screen_height = (board_ROWS+1)*square_size + screenTopSpace
	screen_size = (screen_width, screen_height)

	# display screen with pygame module
	screen = pygame.display.set_mode(screen_size)
	pygame.display.update()

	# draw our game board on the pygame window
	drawBoard(game_board)

	# track which player needs to make a move already
	player_turn = random.randint(0, 1)
	if player_turn == 1:
		print("Player 2's Turn!")

	else:
		print("Player 1's Turn!")

	# track the total number of moves done by both players
	move = 0

	# format the font of the message that will appear after the game ends
	endGameFont = pygame.font.SysFont("monospace", 35)

	# format the font of button labels (located at the top part of the screen)
	buttonLabelFont = pygame.font.SysFont("monospace", 13)

	# format the font of message that will appear at top-right part of the screen when the user saves the current game state or loaded the last saved state
	stateFont = pygame.font.SysFont("monospace", 17)

	# specify the locations and dimensions of the rectangle buttons that will be displayed at the top part of our screen
	restart_button = pygame.Rect(10, 5, 75, 20)
	save_button = pygame.Rect(126, 5, 100, 20)
	load_button = pygame.Rect(236, 5, 100, 20)
	back_button = pygame.Rect(545, 5, 117, 20)

	# create loops for our program; one for the pygame window and one for the main game
	gameOver = False
	pygame_windowIsRunning = True
	
	# create a loop that will display the pygame window (until a certain termination statement is encountered)
	while pygame_windowIsRunning:
		# assign a variable that will tell us if the user clicks any of the button or not
		# this variable will be used somewhere in the block of codes below
		click = False
		# Since pygame is an event-based game library (reads all movements (e.g key presses, mouse movements, mouse clicks, etc.) as individual events)
		# We'll create a loop that assess each event happening in our pygame window
		for event in pygame.event.get():
			# if the user clicks the x/quit button on the pygame's window, then the program will be terminated
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
			# pos, button = event attributes defined with the event type MOUSEBUTTONDOWN
				if event.button == 1:
					click = True

		# create a loop for the main game's behavior
		while not gameOver:
			# assign a variable that will tell us if the user clicks any of the button or not
			# this variable will be used somewhere in the block of codes below
			click = False
			for event in pygame.event.get():
				# draw a black rectangle on the top row of the screen to reset the display of the top row every time an event takes place on that part of the screen
				pygame.draw.rect(screen, BLACK, (0, screenTopSpace, screen_width, square_size))
				
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				# animates a colored piece at the top part of our pygame window
				if event.type == pygame.MOUSEMOTION:
					# pos is an attribute defined with the event type MOUSEMOTION
					x_coordinate = event.pos[0]

					# Display colored piece on the top row of the screen		
					if player_turn == 0:
						pygame.draw.circle(screen, RED, (x_coordinate, screenTopSpace + int(square_size/2)), radiusOfPiece)
						
					else:
						pygame.draw.circle(screen, YELLOW, (x_coordinate, screenTopSpace + int(square_size/2)), radiusOfPiece)
						
					pygame.display.update()

				# drop a colored piece if the user clicks the left mouse button
				if event.type == pygame.MOUSEBUTTONDOWN:
					# pos, button = event attributes defined with the event type MOUSEBUTTONDOWN

					if event.button == 1:
						# event.pos is a tuple with 2 elements each corresponds to the x and y coordinates respectively
						x_coordinate = event.pos[0]
						y_coordinate = event.pos[1]

						if y_coordinate > screenTopSpace:
							# Ask for Player 1's Move
							if player_turn == 0:
								column = x_coordinate//square_size

								if isFree(game_board, column):
									row = getTheAvailableRow(game_board, column)
									dropPiece(game_board, row, column, 1)
									
									# update the total number of moves
									move += 1

									# update the game board display on the commandline interface and on the pygame's window
									printBoard(game_board)
									drawBoard(game_board)

									player_turn += 1 					# increment the value of the variable player turn by 1 so each player changes turn
									player_turn = player_turn%2 		# use the modulo operation so the value of player_turn will always be either 0 or 1 only

									# inform the players whose turn is it already
									if not gameOver:
										if player_turn == 1:
											print("Player 2's Turn!")

										else:
											print("Player 1's Turn!")

								# this else statement prohibits a player to drop a piece on a column with no available slots already
								else:
									continue

							# Ask for Player 2's Move
							else:			
								column = x_coordinate//square_size

								if isFree(game_board, column):
									row = getTheAvailableRow(game_board, column)
									dropPiece(game_board, row, column, 2)

									# update the total number of moves
									move += 1

									# update the game board display on the commandline interface and on the pygame's window
									printBoard(game_board)
									drawBoard(game_board)

									player_turn += 1 					# increment the value of the variable player turn by 1 so each player changes turn
									player_turn = player_turn%2 		# use the modulo operation so the value of player_turn will always be either 0 or 1 only

									# inform the players whose turn is it already
									if not gameOver:
										if player_turn == 1:
											print("Player 2's Turn!")

										else:
											print("Player 1's Turn!")

								else:
									continue
						

						# if the mouse click is made on the screenTopSpace surface, set the click variable to True
						else:
							click = True

						# draw a black rectangle to cover up the message that will appear when the user clicks the save state or the load state button
						pygame.draw.rect(screen, BLACK, (340, 0, 200, 28))

					# this else statement prohibits other mouse buttons to do anything in our program		
					else:
						continue


					# End the game if someone wins
					if winningMove(game_board, 1) == True:
						# Display a message if Player 1 wins the game
						endGameCaption = endGameFont.render("Player 1 Wins!", 1, RED)
						screen.blit(endGameCaption, (193, screenTopSpace + 9))
						totalMoves = endGameFont.render("Total Game Moves: " + str(move), 1, GREEN)
						screen.blit(totalMoves, (130, screenTopSpace + 52))

						gameOver = True

						# print a message in the commandline interface
						print("Player 1 Wins!")
						print("Total game moves:", move)

						# open a file for writing (This will replace the stored data on the last_game_played_6x7.txt)
						fileHandle = open("assets/records/last_played_game_6x7.txt", "w")
						# store the results of the last game in a string
						lastGame = "Player 1 Won ..... " + "Total game moves: " + str(move)
						# replace the data stored in the file with the results of the last played game
						fileHandle.write(lastGame)
						# close our fileHandle
						fileHandle.close()

					if winningMove(game_board, 2) == True:
						# Display a message if Player 2 wins the game
						endGameCaption = endGameFont.render("Player 2 Wins!", 1, YELLOW)
						screen.blit(endGameCaption, (193, screenTopSpace + 9))
						totalMoves = endGameFont.render("Total Game Moves: " + str(move), 1, GREEN)
						screen.blit(totalMoves, (130, screenTopSpace + 52))				

						gameOver = True

						# print a message in the commandline interface
						print("Player 2 Wins!")
						print("Total game moves:", move)

						# open a file for writing (This will replace the stored data on the last_game_played_6x7.txt)
						fileHandle = open("assets/records/last_played_game_6x7.txt", "w")
						# store the results of the last game in a string
						lastGame = "Player 2 Won ..... " + "Total game moves: " + str(move)
						# replace the data stored in the file with the results of the last played game
						fileHandle.write(lastGame)
						# close our fileHandle
						fileHandle.close()

					# Also end the game if all empty slots in the gameboard have already been filled up by players' pieces
					zeroNotInRow = 0
					for pieceRow in game_board:
						if 0 not in pieceRow:
							zeroNotInRow +=1

					if zeroNotInRow == board_ROWS:
						# Display a message if the game is a draw
						endGameCaption = endGameFont.render("DRAW!", 1, BLUE)
						screen.blit(endGameCaption, (285, screenTopSpace + 9))
						totalMoves = endGameFont.render("Total Game Moves: " + str(move), 1, GREEN)
						screen.blit(totalMoves, (130, screenTopSpace + 52))

						gameOver = True

						# print a message in the commandline interface				
						print("Draw!")
						print("Total game moves:", move)

						# open a file for writing (This will replace the stored data on the last_game_played_6x7.txt)
						fileHandle = open("assets/records/last_played_game_6x7.txt", "w")
						# store the results of the last game in a string
						lastGame = "Draw ..... " + "Total game moves: " + str(move)
						# replace the data stored in the file with the results of the last played game
						fileHandle.write(lastGame)
						# close our fileHandle
						fileHandle.close()

					pygame.display.update()
				# end of for loop in pygame events

			# draw the rectangle buttons that we specify earlier
			# determine if our mouse cursor touches the rectangle buttons 
			x_mouse, y_mouse = pygame.mouse.get_pos()

			# if the user clicks the restart button, restart the whole program
			if restart_button.collidepoint((x_mouse, y_mouse)):
				pygame.draw.rect(screen, GREEN, restart_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("RESTART", 1, GREEN)
				screen.blit(label, (20, 8))

				if click:
					connect4()
					break

			else:
				pygame.draw.rect(screen, WHITE, restart_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("RESTART", 1, WHITE)
				screen.blit(label, (20, 8))

			# if the user clicks the save state button, save the current state of the game to a file
			if save_button.collidepoint((x_mouse, y_mouse)):
				pygame.draw.rect(screen, GREEN, save_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("SAVE STATE", 1, GREEN)
				screen.blit(label, (136, 8))

				if click:
					saveState(game_board, player_turn, move)
					print("\n\nCurrent game state has been saved successfully!", end="\n\n\n")
					label = stateFont.render("SAVED SUCCESSFULLY!", 1, GREEN)
					screen.blit(label, (346, 5))

			else:
				pygame.draw.rect(screen, WHITE, save_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("SAVE STATE", 1, WHITE)
				screen.blit(label, (136, 8))

			# if the user clicks the load state button, load the last game state that is saved in a file
			if load_button.collidepoint((x_mouse, y_mouse)):
				pygame.draw.rect(screen, GREEN, load_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("LOAD STATE", 1, GREEN)
				screen.blit(label, (246, 8))

				if click:
					game_board = loadState()[0]
					player_turn = loadState()[1]
					move = loadState()[2]
					print("\n\n\n\n\nLast saved state has been successfully loaded!", end="\n\n\n\n\n")
					label = stateFont.render("LOADED SUCCESSFULLY!", 1, GREEN)
					screen.blit(label, (342, 5))
					printBoard(game_board)
					drawBoard(game_board)						
					
					# inform the players whose turn is it already
					if not gameOver:
						if player_turn == 1:
							print("Player 2's Turn!")

						else:
							print("Player 1's Turn!")
					
			else:
				pygame.draw.rect(screen, WHITE, load_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("LOAD STATE", 1, WHITE)
				screen.blit(label, (246, 8))

			# if the user clicks the back to menu button, the game will be closed and will be returned to the main menu screen
			if back_button.collidepoint((x_mouse, y_mouse)):
				pygame.draw.rect(screen, GREEN, back_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("BACK TO MENU", 1, GREEN)
				screen.blit(label, (555, 8))

				if click:
					gameOver = True
					pygame_windowIsRunning = False
					
			else:
				pygame.draw.rect(screen, WHITE, back_button, 3, -1, -1, -1, -1)
				label = buttonLabelFont.render("BACK TO MENU", 1, WHITE)
				screen.blit(label, (555, 8))

			pygame.display.update()
			# end of the while loop not gameOver

		# draw a black rectangle to cover up the save state button when the game ends
		pygame.draw.rect(screen, BLACK, (124, 3, 105, 25))

		# draw the rectangle buttons that we specify earlier
		# determine if our mouse cursor touches the rectangle buttons 
		x_mouse, y_mouse = pygame.mouse.get_pos()

		# if the user clicks the restart button, restart the whole program
		if restart_button.collidepoint((x_mouse, y_mouse)):
			pygame.draw.rect(screen, GREEN, restart_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("RESTART", 1, GREEN)
			screen.blit(label, (20, 8))

			if click:
				connect4()
				break

		else:
			pygame.draw.rect(screen, WHITE, restart_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("RESTART", 1, WHITE)
			screen.blit(label, (20, 8))

		# if the user clicks the load state button, load the last game state that is saved in a file
		if load_button.collidepoint((x_mouse, y_mouse)):
			pygame.draw.rect(screen, GREEN, load_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("LOAD STATE", 1, GREEN)
			screen.blit(label, (246, 8))

			if click:
				game_board = loadState()[0]
				player_turn = loadState()[1]
				move = loadState()[2]
				print("\n\n\n\n\nLast saved state has been successfully loaded!", end="\n\n\n\n\n")
				label = stateFont.render("LOADED SUCCESSFULLY!", 1, GREEN)
				screen.blit(label, (342, 5))
				printBoard(game_board)
				drawBoard(game_board)
				gameOver = False

				# inform the players whose turn is it already
				if not gameOver:
					if player_turn == 1:
						print("Player 2's Turn!")

					else:
						print("Player 1's Turn!")

		else:
			pygame.draw.rect(screen, WHITE, load_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("LOAD STATE", 1, WHITE)
			screen.blit(label, (246, 8))

		# if the user clicks the back to menu button, the game will be closed and will be returned to the main menu screen
		if back_button.collidepoint((x_mouse, y_mouse)):
			pygame.draw.rect(screen, GREEN, back_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("BACK TO MENU", 1, GREEN)
			screen.blit(label, (555, 8))

			if click:
				pygame_windowIsRunning = False
				
		else:
			pygame.draw.rect(screen, WHITE, back_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("BACK TO MENU", 1, WHITE)
			screen.blit(label, (555, 8))

		pygame.display.update()
		# end of the while loop for pygame