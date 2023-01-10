# acces specifiers valid for methods/variables
#naming rules same for variables method and class name 
#public can be accessed anywhere (. operator /method etc)
#protected cannot access it outside the class except for  inheritence 
# denoted by single underscore(_)
#without inheritence private and protected are almost the same
#private cannot access it outside the class denoted by double underscore
#it is accessible inside the class 
#in the biginning


class A:
    __BankName="ICICI"
    def __init__(self,accname1,pwd1):
        self.accname=accname1 #public
        self.__pwd=pwd1#private
    def accesspwd(self):
        print(self.__pwd)
    def __x(self):
        pass
obj1=A("Sagar",56)
#print(obj1.pwd)
print(obj1.accname)
obj1.accesspwd()
