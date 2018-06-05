
visited = [[[[[0 for a in range(8)] for b in range(8)] for k in range(8)] for i in range(8)] for j in range(8)]

class answer:
	def __init__(self , leftc , leftm , rightc , rightm , dirr):
		self.leftc=leftc
		self.leftm=leftm
		self.rightc=rightc
		self.rightm=rightm
		self.dirr=dirr

	def display(self):
		if self.dirr==1:
			print '<'+str(self.leftc)+' '+str(self.leftm)+'>   <---   <'+str(self.rightc)+' '+str(self.rightm)+'>'
		else:
			print '<'+str(self.leftc)+' '+str(self.leftm)+'>   --->   <'+str(self.rightc)+' '+str(self.rightm)+'>'



def valid(c , m ):
	if(c<0 or m<0):
		return False
	if(m==0):
		return True
	if(c>m ):
		return False
	return True

myans=[]

def dfs(leftc , leftm ,rightc , rightm ,boat):
	visited[leftc][leftm][rightc][rightm][boat]=1
	#print str(leftc)+' '+str(leftm)+'     '+str(rightc)+'   '+str(rightm)+'      '+str(boat)
	if(valid(leftc , leftm)==False or valid(rightc , rightm)==False):
	#	print 'hi'
		return False
	if(leftc==0 and leftm==0 and rightc==3 and rightm==3):
		myans.append(answer(leftc , leftm , rightc , rightm , boat))
		return True

	if(boat==0): #left
		if(valid(leftc-1 , leftm) and valid(rightc+1, rightm) and visited[leftc-1][leftm][rightc+1][rightm][boat^1]==0 and dfs(leftc-1 , leftm, rightc+1 , rightm, boat^1)==True):	
			myans.append(answer(leftc , leftm , rightc , rightm  , boat))				
			return True
		if(valid(leftc-1 , leftm-1) and valid(rightc+1, rightm+1) and visited[leftc-1][leftm-1][rightc+1][rightm+1][boat^1]==0 and dfs(leftc-1 , leftm-1 , rightc+1 , rightm+1 , boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm   , boat))
			return True
		#print str(valid(leftc-2 , leftm))+' '+str(valid(leftc+2, leftm))+' '+str(visited[leftc-2][leftm][rightc+2][rightm][boat^1])
		if(valid(leftc-2 , leftm) and valid(rightc+2, rightm) and visited[leftc-2][leftm][rightc+2][rightm][boat^1]==0 and dfs(leftc-2 , leftm , rightc+2, rightm, boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm  , boat))
			return True
		if(valid(leftc , leftm-2) and valid(rightc, rightm+2) and visited[leftc][leftm-2][rightc][rightm+2][boat^1]==0 and dfs(leftc , leftm-2 , rightc , rightm+2 , boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm  , boat))
			return True
	else:
		if(valid(leftc+1 , leftm) and valid(rightc-1, rightm) and visited[leftc+1][leftm][rightc-1][rightm][boat^1]==0 and dfs(leftc+1 , leftm, rightc-1 , rightm, boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm  , boat))
			return True
		if(valid(leftc+1 , leftm+1) and valid(rightc-1, rightm-1) and visited[leftc+1][leftm+1][rightc-1][rightm-1][boat^1]==0 and dfs(leftc+1 , leftm+1 , rightc-1 , rightm-1 , boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm  , boat))
			return True
		if(valid(leftc+2 , leftm) and valid(rightc-2, rightm) and visited[leftc+2][leftm][rightc-2][rightm][boat^1]==0 and dfs(leftc+2 , leftm , rightc-2, rightm, boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm , boat))
			return True
		if(valid(leftc, leftm+2) and valid(rightc, rightm-2) and visited[leftc][leftm+2][rightc][rightm-2][boat^1]==0 and dfs(leftc , leftm+2 , rightc , rightm-2 , boat^1)==True):
			myans.append(answer(leftc , leftm , rightc , rightm  , boat))
			return True
	return False	

print 'c m     c m    boat'
print dfs(5 , 5 , 0 , 0 , 0)

for obj in reversed(myans):
	obj.display()