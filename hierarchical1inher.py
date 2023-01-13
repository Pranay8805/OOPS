"""

Hierarchical inheritence-- one parent and more than one child
"""

class A:
    def p(self):
        print("print p A")
class B(A):
    def p(self):
        print("print p B")
class C(A):
    def p(self):
        print("print p C")
        
obj1=B()
obj1.p()
obj2=C()
obj2.p()
obj3=A()
obj3.p()
