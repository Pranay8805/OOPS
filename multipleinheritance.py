class father:
    def fdisplay(self):
        print("FATHER CLASS")
class mother:
    def mdisplay(self):
        print("MOTHER CLASS")
class child(father,mother):
    def cdisplay(self):
        print("CHILD CLASS")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.fdisplay()


        #multilevel inheritance
        
class father():
    def fdisplay(self):
        print("father class")
class mother():
    def mdisplay(self):
        print("mother class")
class child(father,mother):
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.fdisplay()