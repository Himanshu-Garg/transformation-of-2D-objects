"""

name - himanshu garg
roll no.- 2081337
sec - B
grp - 2

"""




import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse as ell
from SimpleGraphics import *



def multiplymatrix(left,right):
	#left and right means left matrix and right matrix to multiply and return new values

	newmatrix=[]						#used to store final result
	for i in range(len(left)):
		sum=0
		for j in range(len(left[0])):
			sum=sum+(left[i][j]*right[j][0])
		newmatrix.append([sum])

	return newmatrix[0][0],newmatrix[1][0]				



def plottingpolygon(x,y):
	
	maxx=max(max(x),max(y))					#find biggest no. in x and y
	MakeWindow(maxx+4,labels=True,bgcolor=WHITE)
	DrawPoly(x,y, FillColor=None, EdgeWidth=1, EdgeColor=BLACK)			#draw polygon with x and y vertices given as list
	ShowWindow(time=None)

def plottingellipse(x,y,rh,rv,an):
	

	ellipse=ell((x,y),rh*2,rv*2,angle=an)
	fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
	ax.add_artist(ellipse)
	ax.set_xlim(-30, 30)
	ax.set_ylim(-30, 30)
	plt.show()



"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""





class disc():
	def __init__(self,x,y,rh,rv):
		"""
		
		attributes :-

		x : x coordinate of centre
		y : y coordinate of centre
		rx : radius in horizontal direction
		rv : radius in vertical direction
		angle : angle by which it has to be rotated
		"""

		self.x=x
		self.y=y
		self.rh=rh
		self.rv=rv
		self.angle=0


	def __str__(self):
		"""
		return centre coordinatees and two radius  in desired format
		"""
		return str(self.x) + "  " + str(self.y) + "  " + str(self.rh) + "  " + str(self.rv) + "  " + str(self.angle)


	def scaling(self,X,Y):
		"""
		here, X and Y are scaling multiples of x and y axis
		"""
		matrixleft=[]				#left matrix to multiply
		
		matrixleft.append([X,0])
		matrixleft.append([0,Y])

		
		matrixright=[[self.rh],[self.rv]]				#contains x,y in right matrix to multiply
		self.rh,self.rv=multiplymatrix(matrixleft,matrixright)				#function multiplies two matrices

	def rotation(self,theta):
		"""
		theta=angle by which each point has to be rotated
		"""
		
		thetaneeded=(theta/180)*math.pi			#theta that has to go in cos nad sin functions
		
		self.angle+=theta
		matrixleft=[]				#left matrix to multiply
		matrixleft.append([math.cos(thetaneeded),-math.sin(thetaneeded)])
		matrixleft.append([math.sin(thetaneeded),math.cos(thetaneeded)])

		
		matrixright=[[self.x],[self.y]]				#contains x,y in right matrix to multiply
		self.x,self.y=multiplymatrix(matrixleft,matrixright)

	def translation(self,dx,dy):
		"""
		dx and dy has to be added to x and y resp
		"""

		matrixleft=[]				#left matrix to multiply
		matrixleft.append([1,0,dx])
		matrixleft.append([0,1,dy])
		matrixleft.append([0,0,1])

		matrixright=[[self.x],[self.y],[1]]				#contains x,y in right matrix to multiply
		self.x,self.y=multiplymatrix(matrixleft,matrixright)






"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""





class polygon():
	def __init__(self,x,y):
		"""
		arguments are : x and y represents x and y list of coordinates
		"""
		self.x=x
		self.y=y

	
	def __str__(self):
		"""
		return x and y in desired format
		"""
		a=""
		b=""
		for i in range(len(self.x)):
			a=a+str(self.x[i])+"  " 
		
		for i in range(len(self.y)):
			b=b+str(self.y[i])+"  "

		return a+"\n"+b





	def scaling(self,X,Y):
		"""
		here, X and Y are scaling multiples of x and y axis
		"""
		matrixleft=[]				#left matrix to multiply
		
		matrixleft.append([X,0])
		matrixleft.append([0,Y])

		for i in range(len(self.x)):
			matrixright=[[self.x[i]],[self.y[i]]]				#contains x,y in right matrix to multiply
			self.x[i],self.y[i]=multiplymatrix(matrixleft,matrixright)				#function multiplies two matrices

	def rotation(self,theta):
		"""
		theta=angle by which each point has to be rotated
		"""
		
		thetaneeded=(theta/180)*math.pi			#theta that has to go in cos nad sin functions
		
		matrixleft=[]				#left matrix to multiply
		matrixleft.append([math.cos(thetaneeded),-math.sin(thetaneeded)])
		matrixleft.append([math.sin(thetaneeded),math.cos(thetaneeded)])

		for i in range(len(self.x)):
			matrixright=[[self.x[i]],[self.y[i]]]				#contains x,y in right matrix to multiply
			self.x[i],self.y[i]=multiplymatrix(matrixleft,matrixright)	


	def translation(self,dx,dy):
		"""
		dx and dy has to be added to x and y resp
		"""

		matrixleft=[]				#left matrix to multiply
		matrixleft.append([1,0,dx])
		matrixleft.append([0,1,dy])
		matrixleft.append([0,0,1])

		for i in range(len(self.x)):
			matrixright=[[self.x[i]],[self.y[i]],[1]]				#contains x,y in right matrix to multiply
			self.x[i],self.y[i]=multiplymatrix(matrixleft,matrixright)	




"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""






if __name__=="__main__":
	
	print("enter the shape (disc or polygon) : ",end="")
	shape=input()											#input disc or polygon
	
				#---------------------------------------------------------------------------------------------------------------------

	if shape=="disc":

		angle=0									#used to store angle by which ellipse has to be rotated anti clock wise
		b=input()								#contains a b r space-seperated
		b=list(map(float,b.split(" ")))
		b.append(b[-1])						#so that b has a b r r i.e 2 r

		dis=disc(b[0],b[1],b[2],b[3])
		plottingellipse(dis.x,dis.y,dis.rh,dis.rv,angle)

		instruct="a"						#used to store commands given to it
		print("queries can be of the form :")
		print("S x y")
		print("R theta")
		print("T dx dy")
		print()
		
		while instruct != "quit":				#runs until instruction is not equal to quit
			instruct=input("enter command : ")
			ins=list(map(str,instruct.split(" ")))			#contains instruction in list form
			if instruct[0]=="S":
				dis.scaling(float(ins[1]),float(ins[2]))
				print(dis)
				plottingellipse(dis.x,dis.y,dis.rh,dis.rv,angle)
			elif instruct[0]=="R":
				dis.rotation(float(ins[1]))
				angle=angle+float(ins[1])					#update angle
				print(dis)
				plottingellipse(dis.x,dis.y,dis.rh,dis.rv,angle)
			elif instruct[0]=="T":
				dis.translation(float(ins[1]),float(ins[2]))
				print(dis)
				plottingellipse(dis.x,dis.y,dis.rh,dis.rv,angle)
		

				#---------------------------------------------------------------------------------------------------------------------


	elif shape=="polygon":
		b=input()						#contains x[] space seperated
		c=input()						#contains y[] space seperated
		x=list(map(float,b.split(" ")))		#contains x coortinated of polygon
		y=list(map(float,c.split(" ")))		#contains y coordinateds of polygon

		
		
		instruct="a"						#used to store commands given to it
		print("queries can be of the form :")
		print("S x y")
		print("R theta")
		print("T dx dy")
		print()
		
		poly=polygon(x,y)

		plottingpolygon(poly.x,poly.y)
		while instruct != "quit":				#runs until instruction is not equal to quit
			instruct=input("enter command : ")
			ins=list(map(str,instruct.split(" ")))			#contains instruction in list form
			if instruct[0]=="S":
				poly.scaling(float(ins[1]),float(ins[2]))
				print(poly)
				plottingpolygon(poly.x,poly.y)
			elif instruct[0]=="R":
				poly.rotation(float(ins[1]))
				print(poly)
				plottingpolygon(poly.x,poly.y)
			elif instruct[0]=="T":
				poly.translation(float(ins[1]),float(ins[2]))
				print(poly)
				plottingpolygon(poly.x,poly.y)

	#---------------------------------------------------------------------------------------------------------------------

	else:
		print("wrong shape entered")

