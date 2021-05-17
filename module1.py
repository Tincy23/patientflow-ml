class module:
	def __init__(self):
		self.a=0
		self.b=""
	def read(self):
		self.a=int(input("enter the number"))
		self.b=input("enter a string")
	def print(self):
		print("enter number",self.a)
		print("enter string",self.b)
	
