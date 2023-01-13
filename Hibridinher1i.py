#Hibrid Inheritence
class A(object):
    def p(self):
        print("print p A")
class B(A):
    def pB(self):
        print("print p B")
class C(A):
    def pC(self):
        print("print p C")
class D(B,C):
    def pD(self):
        print("print p D")
obj1=D()
obj1.p()
obj2=B()
obj2.p()
obj3=C()
obj3.p()
obj4=A()
obj4.p()

print(B.mro())
print(C.mro())
print(D.mro())
print(A.mro())

"""

MRO--Method Resolution Order
we try to serach on the same level first
"""

class A: 
    def p(self):
        print("print p A")
class B(A):
    def pb(self):        
        print("print p B")        
class C(A):  
    def p(self):
        print("print p C")        
obj1=B()
obj1.p()
obj2=C()
obj2.p()

#It searched for the implementation in the Inheritence Tree