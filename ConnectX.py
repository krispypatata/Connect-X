import pygame
import sys
from assets import connect4
from assets import connect5
from assets import about_menu

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
# format the font of our title
title_font = pygame.font.Font("assets/fonts/agency_regular.ttf", 100)

# set the dimensions of our rectangle buttons
connect4_button = pygame.Rect(175, 250, 322, 100)
connect5_button = pygame.Rect(175, 400, 322, 100)
exit_button = pygame.Rect(175, 550, 322, 100)

connect4_inside = pygame.Rect(176, 251, 320, 98)
connect5_inside = pygame.Rect(176, 401, 320, 98)
exit_inside = pygame.Rect(176, 551, 320, 98)

# rectangle buttons for the title area
title_button = pygame.Rect(168, 111, 340, 80)
title_inside = pygame.Rect(168, 111, 340, 80)

# load the background image from a folder
background_image = pygame.image.load("assets/images/background.png").convert()

# this variable below (click) will only return true if the user clicks a certain rectangle button in our pygame window
click = False

# create a loop for our main menu window
# the loop will only be terminated if the user chooses to exit our program
while True:
	# always fill the screen with the background image
	screen.blit(background_image, (0,0))

	# get the present position of our mouse pointer on the pygame window
	x_mouse, y_mouse = pygame.mouse.get_pos()

	# draw rectangles on the pygame window for for each button in our main menu screen
	# check if our mouse pointer touches our any rectangle button
	# change the color of a rectangle button whenever our mouse pointer touches it
	# display text inside our rectangle buttons

	# button for our connect 4 game (connect four discs to win - 6x7 board)
	if connect4_button.collidepoint((x_mouse, y_mouse)):
		pygame.draw.rect(screen, DARKGREEN, connect4_inside)
		pygame.draw.rect(screen, GREEN, connect4_button, 10, -1, -1, -1, -1)
		label = button_labelFont.render("CONNECT 4", 1, GREEN)
		screen.blit(label, (200, 270))
		
		
		# if the user clicks the connect4_button, we'll run our game connect4
		if click:
			connect4.connect4()
			pygame.display.update()

	else:
		pygame.draw.rect(screen, WHITE, connect4_button, 10, -1, -1, -1, -1)
		label = button_labelFont.render("CONNECT 4", 1, WHITE)
		screen.blit(label, (200, 270))
		

	# button for our connect 5 game (connect five discs to win - 7x8 board)
	if connect5_button.collidepoint((x_mouse, y_mouse)):
		pygame.draw.rect(screen, DARKGREEN, connect5_inside)
		pygame.draw.rect(screen, GREEN, connect5_button, 10, -1, -1, -1, -1)
		label = button_labelFont.render("CONNECT 5", 1, GREEN)
		screen.blit(label, (200, 420))
		
		# if the user clicks the connect5_button, we'll run our game connect5
		if click:
			connect5.connect5()
			pygame.display.update()

	else:
		pygame.draw.rect(screen, WHITE, connect5_button, 10, -1, -1, -1, -1)
		label = button_labelFont.render("CONNECT 5", 1, WHITE)
		screen.blit(label, (200, 420))

	# exit button
	if exit_button.collidepoint((x_mouse, y_mouse)):
		pygame.draw.rect(screen, DARKRED, exit_inside)
		pygame.draw.rect(screen, RED, exit_button, 10, -1, -1, -1, -1)
		label = button_labelFont.render("EXIT", 1, RED)
		screen.blit(label, (275, 570))
		
		# if the user clicks the exit_button, we'll exit our program
		if click:
			pygame.quit()
			sys.exit()

	else:
		pygame.draw.rect(screen, WHITE, exit_button, 10, -1, -1, -1, -1)
		label = button_labelFont.render("EXIT", 1, WHITE)
		screen.blit(label, (275, 570))

	# This is for the title area
	# Text will only be displayed here
	if title_button.collidepoint((x_mouse, y_mouse)):
		label = title_font.render("CONNECT X", 1, YELLOW)
		screen.blit(label, (164, 90))
		pygame.display.update()
		
		# if the user clicks the title_button, we'll enter the title program
		if click:
			about_menu.about()
			pygame.display.update()

	else:
		label = title_font.render("CONNECT X", 1, WHITE)
		screen.blit(label, (164, 90))
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


