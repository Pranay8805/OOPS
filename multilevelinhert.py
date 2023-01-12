"""
Multilevel Inheritence

more than two levels
"""
# Base level

class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
        
        
# Intermediate class

class Father(Grandfather):
    def __init__(self, fathername):
        self.fathername = fathername

        
#Derived class
class son(Father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname
        self.fathername=fathername
        self.grandfathername=grandfathername
        
        
    def print_name(self):
       print('Grandfather name :', self.grandfathername)
       print("Father name :", self.fathername)
       print("Son name :", self.sonname)

        
        
#driver code

s1=son('prince','raja','shyam')
s1.print_name()
print(s1.sonname)
print(s1.grandfathername)


#Super.__init__(fathername)

# super is used to access the attributes/method of the parent class