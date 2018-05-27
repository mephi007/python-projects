import os
import time
import random

#def board

board = [ '',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_board():
	print ( '  '+board[1]+ '|'+' '+board[2]+ '|'+' '+ board[3])
	print (" --+--+--")
	print ('  '+board[4]+ '|'+' '+board[5]+ '|'+' '+ board[6])
	print (" --+--+--")
	print ('  '+board[7]+ '|'+' '+board[8]+ '|'+' '+board[9])

def is_tie(board):
	if " " in board:
		return False
	else:
		return True
	
	



def is_winner(board, player):
	if (board[1] == player and board[2] == player and board[3] == player) or \
		(board[4] == player and board[5] == player and board[6] == player) or \
		(board[7] == player and board[8] == player and board[9] == player) or \
		(board[1] == player and board[4] == player and board[7] == player) or \
		(board[2] == player and board[5] == player and board[8] == player) or \
		(board[3] == player and board[6] == player and board[9] == player) or \
		(board[1] == player and board[5] == player and board[9] == player) or \
		(board[3] == player and board[5] == player and board[7] == player):
		return True
	else:
		return False


while True:
	os.system("clear")
	print_board()
	choice= int(raw_input("Please choose an empty space for X. "))

#check the position is available or not
	if board[choice] == " ":
		board[choice]= "X"
	else:
		print "sorry! position already been taken. Try another move"
		time.sleep(1)
		continue
		
		

		
	#Check for X win
	if is_winner(board, "X"):
		os.system("clear")
		
		print_board()
		print "X wins! Congratulations"
		break

	os.system("clear")
	print_board()

	#tie_function
	if is_tie(board):
		print "Tie!"
		break
	
	#Get Player O Input
	
	choice= int(raw_input("Please choose an empty space for O. "))

	
	#Check to see if the space is empty first
	if board[choice] == " ":
		board[choice] = "O"
	else:
		print "Sorry, that space is not empty!"
		time.sleep(1)
		continue
		
		
	#Check for O win
	if is_winner(board, "O"):
		os.system("clear")
		print_board()
		print "O wins! Congratulations"
		break
	
	
	if is_tie(board):
		print "Tie!"
		break