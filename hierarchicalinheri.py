class parent:
    def display(self):
        print("PARENT CLASS")
class child1(parent):
    def c1display(self):
        print("CHILD1 CLASS")
class child2(parent):
    def c2display(self):
        print("CHILD2 CLASS")
c1=child1()
c2=child2()
c1.c1display()
c1.display()
c2.c2display()
c2.display()


        # hierarchical inheritance
        
class parent():
    def display(self):
        print("parent class")
class child1(parent):
    def c1display(self):
        print("child1 class")
    
class child2(parent):
    def c2display(self):
        print("child2 class")
c1=child1()
c2=child2()
c1.c1display()
c1.display()
c2.c2display()
c2.display()
        