import heapq

visited = [[[[[0 for a in range(8)] for b in range(8)] for k in range(8)] for i in range(8)] for j in range(8)]
heap=[]

class answer:
	def __init__(self , leftc , leftm , rightc , rightm , boat):
		self.leftc=leftc
		self.leftm=leftm
		self.rightc=rightc
		self.rightm=rightm
		self.boat=boat

	def display(self):
		if self.boat==1:
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

parent = [[[[[answer(0 , 0 , 0 , 0 , 0) for a in range(8)] for b in range(8)] for k in range(8)] for i in range(8)] for j in range(8)]


def ucs(leftc , leftm , rightc , rightm , boat):
	visited[leftc][leftm][rightc][rightm][boat]=1
	obj=answer(leftc , leftm , rightc , rightm , boat)
	myans.append(obj)
	heapq.heappush(heap , (1 , obj));
	while(heap):
		item=heapq.heappop(heap)
		prioirty=item[0]
		state=item[1]
		leftc=item[1].leftc
		leftm=item[1].leftm
		rightc=item[1].rightc
		rightm=item[1].rightm
		boat=item[1].boat
		#print '<'+str(leftc)+' '+str(leftm)+'>   ---'+str(boat)+'---   <'+str(rightc)+' '+str(rightm)+'>'
		visited[leftc][leftm][rightc][rightm][boat]=1
		if(leftc==0 and leftm==0 and rightc==3 and rightm==3 and boat==1):
			#print '<'+str(parent[0][0][3][3][1].leftc)+' '+str(parent[0][0][3][3][1].leftm)+'>   ---++---   <'+str(parent[0][0][3][3][1].rightc)+' '+str(parent[0][0][3][3][1].rightm)+'>'
			myans.append(answer(leftc , leftm , rightc , rightm , boat))
			return True
		if(boat==0): #left
			if(valid(leftc-1 , leftm) and valid(rightc+1, rightm) and visited[leftc-1][leftm][rightc+1][rightm][boat^1]==0 ):	
				obj=answer(leftc-1 , leftm , rightc+1 , rightm , boat^1)
				heapq.heappush(heap , (1 , obj));
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))				
			if(valid(leftc-1 , leftm-1) and valid(rightc+1, rightm+1) and visited[leftc-1][leftm-1][rightc+1][rightm+1][boat^1]==0):
				obj=answer(leftc-1 , leftm-1 , rightc+1 , rightm+1 ,boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
			#print str(valid(leftc-2 , leftm))+' '+str(valid(leftc+2, leftm))+' '+str(visited[leftc-2][leftm][rightc+2][rightm][boat^1])
			if(valid(leftc-2 , leftm) and valid(rightc+2, rightm) and visited[leftc-2][leftm][rightc+2][rightm][boat^1]==0):
				obj=answer(leftc-2 , leftm , rightc+2 , rightm , boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
			if(valid(leftc , leftm-2) and valid(rightc, rightm+2) and visited[leftc][leftm-2][rightc][rightm+2][boat^1]==0):
				obj=answer(leftc , leftm-2 , rightc , rightm+2 , boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
		else:
			if(valid(leftc+1 , leftm) and valid(rightc-1, rightm) and visited[leftc+1][leftm][rightc-1][rightm][boat^1]==0 ):
				obj=answer(leftc+1 , leftm , rightc-1 , rightm , boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
			if(valid(leftc+1 , leftm+1) and valid(rightc-1, rightm-1) and visited[leftc+1][leftm+1][rightc-1][rightm-1][boat^1]==0 ):
				obj=answer(leftc+1 , leftm+1 , rightc-1 , rightm-1 , boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
			if(valid(leftc+2 , leftm) and valid(rightc-2, rightm) and visited[leftc+2][leftm][rightc-2][rightm][boat^1]==0 ):
				obj=answer(leftc+2 , leftm , rightc-2 , rightm , boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
			if(valid(leftc, leftm+2) and valid(rightc, rightm-2) and visited[leftc][leftm+2][rightc][rightm-2][boat^1]==0 ):
				obj=answer(leftc , leftm+2 , rightc , rightm-2 , boat^1)
				parent[obj.leftc][obj.leftm][obj.rightc][obj.rightm][obj.boat]=(answer(leftc , leftm , rightc , rightm  , boat))
				heapq.heappush(heap , (1 , obj));
				
	return False	


print 'c  m    boat    c  m    '
ucs(3 , 3 , 0 , 0 , 0)

leftc=0
leftm=0
rightc=3
rightm=3
boat=1

while (True):
	if boat==1:
		print '<'+str(leftc)+' '+str(leftm)+'>   <---   <'+str(rightc)+' '+str(rightm)+'>'
	else:
		print '<'+str(leftc)+' '+str(leftm)+'>   --->   <'+str(rightc)+' '+str(rightm)+'>'
	tleftc=parent[leftc][leftm][rightc][rightm][boat].leftc
	tleftm=parent[leftc][leftm][rightc][rightm][boat].leftm
	trightc=parent[leftc][leftm][rightc][rightm][boat].rightc
	trightm=parent[leftc][leftm][rightc][rightm][boat].rightm
	tboat=parent[leftc][leftm][rightc][rightm][boat].boat
	leftc=tleftc
	leftm=tleftm
	rightc=trightc
	rightm=trightm
	boat=tboat
	#if boat==1:
	#	print '<'+str(leftc)+' '+str(leftm)+'>   <---   <'+str(rightc)+' '+str(rightm)+'>'
	#else:
	#	print '<'+str(leftc)+' '+str(leftm)+'>   --->   <'+str(rightc)+' '+str(rightm)+'>'
	if leftc==0 and leftm==0 and rightc==0 and rightm==0 and boat==0:
	#	print 'hi'
		break
	

#for obj in reversed(myans):
#	obj.display()