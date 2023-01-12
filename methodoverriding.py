"""

polymorphism

method overriding

method overriding -- two method with same name different 
defination in two different classes
"""

class A:
    def x(self): #overriden method
        print("this is x of class A")
class B:
    def x(self):#overriding method
        print("this is x of class B")
        
obj1=B()
obj1.x()
obj2=A()
obj2.x()
    

"""

polymorphism-- one name many forms

it works as per class implementation


"""

print(len([2,3,4]))
print(len((2,3,4,5,6,7)))
print(len("Edyoda"))