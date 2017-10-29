import numpy as np
import argparse

N = 5

class Piece:

	def __init__(self, piece_type, position):
		self.piece_type = piece_type
		self.position = position
		self.promoted = False
		self.moveTypes = set([piece_type])

	def __str__(self):
		return "{}{}".format(self.piece_type, ('+' if self.promoted else ''))

	def promote(self):
		if self.piece_type in ['K', 'k', 'g', 'G']:
			return
		self.promoted = True
		if self.piece_type == 'p':
			self.moveTypes = set(['g'])
		elif self.piece_type == 'P':
			self.moveTypes = set(['G'])
		elif self.piece_type == 's':
			self.moveTypes = set(['g'])
		elif self.piece_type == 'S':
			self.moveTypes = set(['G'])
		elif self.piece_type == 'b':
			self.moveTypes.add('k')
		elif self.piece_type == 'B':
			self.moveTypes.add('K')
		elif self.piece_type == 'r':
			self.moveTypes.add('k')
		elif self.piece_type == 'R':
			self.moveTypes.add('K')

	def demote(self):
		if self.piece_type in ['K', 'k', 'g', 'G']:
			return
		self.promoted = False
		self.moveTypes = set([self.piece_type])

	def possible_moves(self, gameBoard):

		all_moves = []
		for moveType in self.moveTypes:
			func = moves[moveType]
			all_moves.extend(func(self.position, gameBoard))
		return all_moves

def notSamePlayer(x1,y1,x2,y2,gameBoard):
	if (gameBoard[x1][y1] is None) or (gameBoard[x2][y2] is None):
		return true
	if gameBoard[x1][y1].piece_type.islower() and gameBoard[x2][y2].piece_type.islower():
		return false
	if gameBoard[x1][y1].piece_type.isupper() and gameBoard[x2][y2].piece_type.isupper():
		return false
	return true

def king_moves(curr_pos, gameBoard):
	
	valid_moves = []
	x = curr_pos[0]
	y = curr_pos[1]

	if (0 <= x+1 < N) and (0 <= y < N) and notSamePlayer(x,y,x+1,y,gameBoard):
		valid_moves.append((x+1,y))
	if (0 <= x+1 < N) and (0 <= y+1 < N) and notSamePlayer(x,y,x+1,y+1,gameBoard):
		valid_moves.append((x+1,y+1))
	if (0 <= x+1 < N) and (0 <= y-1 < N) and notSamePlayer(x,y,x+1,y-1,gameBoard):
		valid_moves.append((x+1,y-1))
	if (0 <= x < N) and (0 <= y+1 < N) and notSamePlayer(x,y,x,y+1,gameBoard):
		valid_moves.append((x,y+1))
	if (0 <= x < N) and (0 <= y-1 < N) and notSamePlayer(x,y,x,y-1,gameBoard):
		valid_moves.append((x,y-1))
	if (0 <= x-1 < N) and (0 <= y < N) and notSamePlayer(x,y,x-1,y,gameBoard):
		valid_moves.append((x-1,y))
	if (0 <= x-1 < N) and (0 <= y+1 < N) and notSamePlayer(x,y,x-1,y+1,gameBoard):
		valid_moves.append((x-1,y+1))
	if (0 <= x-1 < N) and (0 <= y-1 < N) and notSamePlayer(x,y,x-1,y-1,gameBoard):
		valid_moves.append((x-1,y-1))

	return valid_moves

def rook_moves(curr_pos, gameBoard):

	valid_moves = []
	x1 = curr_pos[0]
	y1 = curr_pos[1]

	for i in range(1,5):
		x2 = x1 - i
		y2 = y1
		if not (0 <= x2 < N):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))
	
	for i in range(1,5):
		x2 = x1 + i
		y2 = y1
		if not (0 <= x2 < N):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))

	for i in range(1,5):
		y2 = y1 - i
		x2 = x1
		if not (0 <= y2 < N):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))

	for i in range(1,5):
		y2 = y1 + i
		x2 = x1
		if not (0 <= y2 < N):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))


	return valid_moves

def bishop_moves(curr_pos, gameBoard):

	valid_moves = []
	x1 = curr_pos[0]
	y1 = curr_pos[1]

	for i in range(1,5):
		x2 = x1 + i
		y2 = y1 + i
		if not ((0 <= x2 < N) and (0 <= y2 < N)):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))

	for i in range(1,5):
		x2 = x1 + i
		y2 = y1 - i
		if not ((0 <= x2 < N) and (0 <= y2 < N)):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))

	for i in range(1,5):
		x2 = x1 - i
		y2 = y1 + i
		if not ((0 <= x2 < N) and (0 <= y2 < N)):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))

	for i in range(1,5):
		x2 = x1 - i
		y2 = y1 - i
		if not ((0 <= x2 < N) and (0 <= y2 < N)):
			break
		if (0 <= x2 < N) and (0 <= y2 < N):
			if gameBoard[x2][y2] is not None:
				if notSamePlayer(x1,y1,x2,y2,gameBoard):
					valid_moves.append((x2,y2))
					break
				else:
					break
			else:
				valid_moves.append((x2,y2))

	return valid_moves

def gold_general_moves(curr_pos, gameBoard):

	valid_moves = []
	x = curr_pos[0]
	y = curr_pos[1]

	if gameBoard[x][y].piece_type.islower():
		
		x2 = x-1
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x-1
		y2 = y
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))

	else:

		x2 = x-1
		y2 = y
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x-1
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))

	return valid_moves

def silver_general_moves(curr_pos, gameBoard):

	valid_moves = []
	x = curr_pos[0]
	y = curr_pos[1]

	if gameBoard[x][y].piece_type.islower():
		
		x2 = x-1
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x-1
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))

	else:

		x2 = x-1
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x-1
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
		x2 = x+1
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))

	return valid_moves

def pawn_moves(curr_pos, gameBoard):
	#if ends up in promotion zone, then promote automatically
	valid_moves = []
	x = curr_pos[0]
	y = curr_pos[1]

	if gameBoard[x][y].piece_type.islower():
		x2 = x
		y2 = y+1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))
	else:
		x2 = x
		y2 = y-1
		if (0 <= x2 < N) and (0 <= y2 < N) and notSamePlayer(x,y,x2,y2,gameBoard):
			valid_moves.append((x2,y2))

	return valid_moves

moves = {'k': king_moves, 'K': king_moves, 'r': rook_moves, 'R': rook_moves, 'b': bishop_moves, 'B': bishop_moves, 'g': gold_general_moves, 'G': gold_general_moves. 's': silver_general_moves, 'S': silver_general_moves, 'p': pawn_moves, 'P': pawn_moves}

def position_to_coord(pos):
	x = int(pos[0] - 'a')
	y = int(pos[1]) - 1
	if x > 4 or y > 4:
		return None
	return (x,y)

def coord_to_pos(coord):
	x = coord[0]
	y = coord[1]
	x = chr('a' + x)
	y = str(y)
	return str(x+y)

def gameBoard_to_stringBoard(gameBoard): #print them as +p and so own if they are promoted
	stringBoard = [[str(gameBoard[i][j]) if gameBoard[i][j] != None else '' for i in range(N)] for j in range(N)]
	return stringBoard

def init_gameBoard(gameBoard):
	gameBoard[0][4] = Piece('R', (0,4))
	gameBoard[1][4] = Piece('B', (1,4))
	gameBoard[2][4] = Piece('S', (2,4))
	gameBoard[3][4] = Piece('G', (3,4))
	gameBoard[4][4] = Piece('K', (4,4))
	gameBoard[4][3] = Piece('P', (4,3))
	gameBoard[0][1] = Piece('p', (0,1))
	gameBoard[0][0] = Piece('k', (0,0))
	gameBoard[1][0] = Piece('g', (1,0))
	gameBoard[2][0] = Piece('s', (2,0))
	gameBoard[3][0] = Piece('b', (3,0))
	gameBoard[4][0] = Piece('r', (4,0))

def move(gameBoard, move_played, lowers_turn, promote = False):
	#if pawn moves into the promotion zone, automatically promote him
	start_pos = move_played[0]
	end_pos = move_played[1]

	#check if the move is valid
	piece_at_start_pos = gameBoard[start_pos[0]][start_pos[1]]
	if piece_at_start_pos == None:
		return False
	if (piece_at_start_pos.piece_type.islower() and (not lowers_turn)) or (piece_at_start_pos.piece_type.isupper() and lowers_turn):
		return False
	if end_pos not in piece_at_start_pos.possible_moves(gameBoard):
		return False

	#see if any captures are to be done
	if gameBoard[end_pos[0]][end_pos[1]] is not None:
		captured_piece = gameBoard[end_pos[0]][end_pos[1]]
		if lowers_turn:
			lower_captured.append(captured_piece)
		else:
			upper_captured.append(captured_piece)
		captured_piece.position = (-1,-1)

	#update GameBoard and the piece's position
	gameBoard[end_pos[0]][end_pos[1]] = piece_at_start_pos
	gameBoard[start_pos[0]][start_pos[1]] = None
	piece_at_start_pos.position = end_pos

	#promotion check
	if promote and ((lowers_turn and end_pos[1] != 4) or (!lowers_turn and end_pos[1] != 0)):
		return False

	if promote or (piece_at_start_pos.piece_type == 'p' and end_pos[1] == 4) or (piece_at_start_pos.piece_type == 'P' and end_pos[1] == 0):
		piece_at_start_pos.promote()

	return True

def checkDetection(gameBoard, lowers_turn):

	



def validDrop(gameBoard, move):

#def capture(gameBoard, move):







gameBoard = [[None for i in range(N)] for i in range(N)]
lower_captured = []
upper_captured = []

moves_count = 0

