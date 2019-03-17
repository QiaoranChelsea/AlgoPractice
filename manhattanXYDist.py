# 给一个矩阵，寻找Manhattan 距离最短的X和Y
# input：
# X O O O
# O O X Y
# O X O Y

# (p1, p2) = |p2.x – p1.x| + |p2.y – p1.y|.

def manhattanXYDist(grid):
	if not grid or not grid[0]:
		return 

	rows = len(grid)
	cols = len(grid[0])
	qX = []
	qY = [] 
	count = 0 
	deltaX = [0,0,-1,1]
	deltaY = [-1,1,0,0]
	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == 'X':
				qX.append(i)
				qY.append(j)

	while qX and qY:
		tempX = qX 
		tempY = qY
		qX = []
		qY = []
		count += 1 
		while tempX and tempY:
			curX = tempX.pop(0)
			curY = tempY.pop(0)
			for i in range(4):
				nbX = curX + deltaX[i]
				nbY = curY + deltaY[i]

				if 0 <= nbX < rows and 0<=nbY < cols:
					if grid[nbX][nbY] == '0':
						grid[nbX][nbY] = count 
					if grid[nbX][nbY] == 'Y':
						return count 
					qX.append(nbX)
					qY.append(nbY)

	return -1 

grid = [['X','0','X','0'],	
		['0','0','0','0'],
		['0','0','0','Y']]

print(manhattanXYDist(grid))





