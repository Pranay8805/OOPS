"""
Multiple Inheritence

more than 1 parent and 1 child class
"""


#base class.

class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
    
# base class2

class Father:
	fathername = ""
	def father(self):
		print(self.fathername)
        
#derived class

class Son(Mother,Father):
    def parents(self):
        print("Father:",self.fathername)
        print("Mother:",self.mothername)
        
s1=Son()

s1.fathername="Raja"
s1.mothername="sita"
s1.parents()