class grandparent:
    def gdisplay(self):
        print("GRANDPARENT CLASS")
class parent(grandparent):
    def pdisplay(self):
        print("PARENT CLASS ")
class child(parent):
    def cdisplay(self):
        print("CHILD CLASS")
        
c1=child()
c1.gdisplay()
c1.pdisplay()
c1.cdisplay()






#multilevel inheritance


class grandparent:
    def gdisplay(self):
        print("grandparent")
class parent(grandparent):
    def pdisplay(self):
        print("parent class")
class child(parent):
    def cdisplay(self):
        print("child class")
c1=child()
c1.gdisplay()
c1.pdisplay()
c1.cdisplay()