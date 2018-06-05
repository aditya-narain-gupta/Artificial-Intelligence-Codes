import random

class Input :
	def __init__(self  , x_coordinate , y_coordinate):
		self.x=x_coordinate
		self.y=y_coordinate
		if(grid[self.x][self.y]==1):
			self.status="DIRTY"
		else :
			self.status="CLEAN"

def COMPUTE_GRID():
	for i in range ( 0 , m):
		for j in range ( 0 , n):
			number=random.randint(1 , 100)
			if(number <=100*prob[i][j]):
				grid[i][j]=1
			else :
				grid[i][j]=0
			print str(grid[i][j])+' ',
		print ' '	


def printgrid():
	for i in range ( 0 , m):
		for j in range ( 0 , n):
			print str(grid[i][j])+' ',
		print ' '	


def INTERPRET_INPUT(percept):
	#print str(percept.x)+'  '+str(percept.y)
	n=random.randint(0,3)
	#print n
	if(percept.status == "DIRTY"):
		return 4
	if (n==0 and percept.x>0):
		return 0 #MOVE left
	elif (n==0):
		return INTERPRET_INPUT(percept)
	if (n==1 and percept.x<m-1):
		return 1#MOVE right
	elif(n==1):
		return INTERPRET_INPUT(percept)
	if (n==2 and percept.y<n-1):
		return 2#MOVE down
	elif (n==2):
		return INTERPRET_INPUT(percept)
	if (n==3 and percept.y>0):
		return 3#move up
	elif (n==3):
		return INTERPRET_INPUT(percept)


def check():
	for i in range ( 0 , m):
		for j in range ( 0 , n):
			if(grid[i][j]!=0):
				return False
	return True


def SIMPLE_REFLEX_AGENT(percept):
	if(check()==True):
		return 
	state = INTERPRET_INPUT(percept)

	if(state==0) :
		new_percept=Input(percept.x-1 , percept.y)
		print 'move left  '+str(new_percept.y)+'  '+str(new_percept.x)
		SIMPLE_REFLEX_AGENT(new_percept)
	elif (state==1) :
		new_percept=Input(percept.x+1 , percept.y)
		print 'move right '+str(new_percept.y)+'  '+str(new_percept.x)
		SIMPLE_REFLEX_AGENT(new_percept)
	elif (state==2) :
		new_percept=Input(percept.x , percept.y+1)
		print 'move down  '+str(new_percept.y)+'  '+str(new_percept.x)
		SIMPLE_REFLEX_AGENT(new_percept)
	elif (state==3) :
		new_percept=Input(percept.x , percept.y-1)
		print 'move up    '+str(new_percept.y)+'  '+str(new_percept.x)
		SIMPLE_REFLEX_AGENT(new_percept)
	elif (state==4) :
		grid[percept.x][percept.y]=0
		new_percept=Input(percept.x, percept.y)
		print 'suck dirt  '+str(new_percept.y)+'  '+str(new_percept.x)+'  '+new_percept.status
		SIMPLE_REFLEX_AGENT(new_percept)
		

m= int (input())
n= int (input())

grid = [[ 0 for i in range ( 0 , n ) ] for j in range (0 , m)]
prob = [[ 0 for i in range ( 0 , n ) ] for j in range ( 0 , m )]
for i in range ( 0 , m ): 
	for j in range ( 0 ,n ) : 
		prob[i][j] = float(input())

COMPUTE_GRID()
coor_x=int(input())
coor_y=int(input())

percept=Input(coor_x , coor_y)
#INTERPRET_INPUT(percept)
SIMPLE_REFLEX_AGENT ( percept)
