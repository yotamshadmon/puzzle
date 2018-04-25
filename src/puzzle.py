import random
	
class pos:
	def __init__(self, i, j):
		self.i = i
		self.j = j
		
class puzzle:
	def __init__(self, n, m, level):
		self.n = n
		self.m = m	
		self.board = [[j*n+i+1 for i in range(0, n)] for j in range(0, m)]
		self.board[m-1][n-1] = 0
		self.blank = pos(n-1, m-1)
		self.shuffle(level)
		
	def validDirs(self, lastMove):
		dirs = []
		if self.blank.i > 0:
			dirs.append('L')
		if self.blank.i < self.n-1:
			dirs.append('R')
		if self.blank.j > 0:
			dirs.append('U')
		if self.blank.j < self.m-1:
			dirs.append('D')
		
		if lastMove != None:
			dirs.remove(self.opositeDir(lastMove))
		
		return dirs
		
	def move(self, dir):
		validMove = 0
		if dir == 'L':
			if self.blank.i-1 >= 0: 
				self.board[self.blank.j][self.blank.i], self.board[self.blank.j][self.blank.i-1] = self.board[self.blank.j][self.blank.i-1], self.board[self.blank.j][self.blank.i]
				self.blank = pos(self.blank.i-1,self.blank.j);
				validMove = 1
		if dir == 'R':
			if self.blank.i+1 < self.n: 
				self.board[self.blank.j][self.blank.i], self.board[self.blank.j][self.blank.i+1] = self.board[self.blank.j][self.blank.i+1], self.board[self.blank.j][self.blank.i]
				self.blank = pos(self.blank.i+1,self.blank.j);
				validMove = 1
		if dir == 'U':
			if self.blank.j-1 >= 0: 
				self.board[self.blank.j][self.blank.i], self.board[self.blank.j-1][self.blank.i] = self.board[self.blank.j-1][self.blank.i], self.board[self.blank.j][self.blank.i]
				self.blank = pos(self.blank.i,self.blank.j-1);
				validMove = 1
		if dir == 'D':
			if self.blank.j+1 < self.m: 
				self.board[self.blank.j][self.blank.i], self.board[self.blank.j+1][self.blank.i] = self.board[self.blank.j+1][self.blank.i], self.board[self.blank.j][self.blank.i]
				self.blank = pos(self.blank.i,self.blank.j+1);
				validMove = 1
		return validMove

	def opositeDir(self, dir):
		if dir == 'U':
			return 'D'
		if dir == 'D':
			return 'U'
		if dir == 'R':
			return 'L'
		if dir == 'L':
			return 'R'

	def shuffle(self, level):
		moveCount = 0
		dir = None
		while moveCount < level:
			dirs = self.validDirs(dir)
			dir = dirs[random.randint(0, len(dirs) - 1)]
			moveCount += self.move(dir)
				
	def printBoard(self):
		for row in self.board:
			for col in row:
				if col == 0:
					print(' ', '\t', end='')
				else:
					print(col,'\t', end='')
			print('\n', end='')
		print('\n', end='')

	def checkBoard(self):
		ret = True
		self.board[self.blank.j][self.blank.i] = self.m * self.n
		for j in range(0, self.m):
			for i in range(0, self.n):
				if self.board[j][i] != j*self.n+i+1:
					ret = False
		self.board[self.blank.j][self.blank.i] = 0
		return ret
		
	def play(self):
		self.printBoard()
		dir = None
		while dir != 'Q':
			dir = input('direction? ').upper()
			self.move(dir)
			self.printBoard()
			if self.checkBoard() == True:
				print('SUCCESS')
				break
	

def main():
	p = puzzle(4, 4, 3)
	p.play()
	
		  
if __name__== "__main__":
  main()
