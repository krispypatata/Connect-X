import pygame
import sys

def about():
	# Colors (r, g, b)
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	YELLOW = (255, 255, 0)
	GREEN = (0, 255, 0)

	DARKGREEN = (0, 25, 0)
	DARKRED = (50, 0, 0)
	DARKBLUE = (0, 0, 25)
	DARKYELLOW = (50, 50, 0)

	# start the pygame library
	pygame.init()

	# set the dimension of our pygame window/screen (Main Menu Window)
	screen_width = 672
	screen_height = 700
	screen_size = (screen_width, screen_height)
	screen = pygame.display.set_mode(screen_size)
	# always initiate the pygame.display.update() function whenever we make changes on the display of our pygame screen
	pygame.display.update()

	# format the font of our button labels
	button_labelFont = pygame.font.SysFont("monospace", 50)
	title_font = pygame.font.Font("assets/fonts/agency_regular.ttf", 50)

	# format the font of the back button label
	buttonLabelFont = pygame.font.SysFont("monospace", 26)

	# format the font of the last game's results
	lastGame_Font = pygame.font.Font("assets/fonts/robotoMono_regular.ttf", 15)

	# display the back button at the upper right part of the screen
	back_button = pygame.Rect(450, 10, 212, 40)

	# load the background image from a folder
	background_image = pygame.image.load("assets/images/background_titleMenu.png").convert()

	# The block of code below opens a file for reading so that the results of the last played game will be displayed in this pygame window
	# First assign an empty string that will store the data from a given file
	lastGame_6x7 = ""
	# open the file last_played_game_6x7.txt for reading
	fileHandle = open("assets/records/last_played_game_6x7.txt", "r")
	# access the data saved in the file and concatenate it in our empty string lastGame_6x7
	for line in fileHandle:
		lastGame_6x7 = lastGame_6x7 + line
	# close our fileHandle
	fileHandle.close()

	# The block of code below opens a file for reading so that the results of the last played game will be displayed in this pygame window
	# First assign an empty string that will store the data from a given file
	lastGame_7x8 = ""
	# open the file last_played_game_6x7.txt for reading
	fileHandle = open("assets/records/last_played_game_7x8.txt", "r")
	# access the data saved in the file and concatenate it in our empty string lastGame_6x7
	for line in fileHandle:
		lastGame_7x8 = lastGame_7x8 + line		
	# close our fileHandle
	fileHandle.close()

	# this variable below (click) will only return true if the user clicks a certain rectangle button in our pygame window
	click = False

	# create a loop for our main menu window
	# the loop will only be terminated if the user chooses to exit our program or if the the variable running become false
	Running = True
	while Running:
		# always fill the screen with the background image
		screen.blit(background_image, (0,0))

		# get the present position of our mouse pointer on the pygame window
		x_mouse, y_mouse = pygame.mouse.get_pos()

		# if the user clicks the back to menu button, the game will be closed and will be returned to the main menu screen
		if back_button.collidepoint((x_mouse, y_mouse)):
			pygame.draw.rect(screen, YELLOW, back_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("BACK TO MENU", 1, YELLOW)
			screen.blit(label, (460, 15))

			if click:
				Running = False

		else:
			pygame.draw.rect(screen, WHITE, back_button, 3, -1, -1, -1, -1)
			label = buttonLabelFont.render("BACK TO MENU", 1, WHITE)
			screen.blit(label, (460, 15))	

		# display the results of the last played games in a particular section in the screen
		label_1 = lastGame_Font.render(lastGame_6x7, 1, WHITE)
		screen.blit(label_1, (100, 530))

		label_2 = lastGame_Font.render(lastGame_7x8, 1, WHITE)
		screen.blit(label_2, (100, 593))

		# update the pygame display
		pygame.display.update()

		click = False
		for event in pygame.event.get():
			# exit our program if the user clicks the top-right exit pygame button
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				# every time a user presses the left-click mouse button, the click variable will return True
				if event.button == 1:
					click = True

				# this else statement prohibits other mouse buttons to do anything in our program
				else:
					continue
