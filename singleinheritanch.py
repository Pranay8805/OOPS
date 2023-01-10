class parent:
    def display(self):
        print("PARENT CLASS")
class child(parent):
    def show(self):
        print("CHILD CLASS")
        
c=child()
c.display()
c.show()


# single inheritance

class parent:
    def display(self):
        print("PARENT CLASS")
class child (parent):
    def show(self):
        print("CHILD CLASS")
c=child()
c.display()
c.show()
