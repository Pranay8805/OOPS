#class opps concept

class BankAccount:
    BankName="HDFC"#class variable
    def __init__(self,accno,accholname,acctype):
        #constructor-construct an object/
        #gives info to the objects/initilize an object
        self.accno=accno
        self.accholname=accholname
        self.acctype=acctype
    def getcc(self):
        
#all instance variable / method need self for reference
      print(self.accholname,"has got the credid card")
    def display(self):
         print(self.accno,self.accholname,self.acctype)
c1=BankAccount(123,"rakesh","savings")
c2=BankAccount(345,"pranay","savings")
c3=BankAccount(956,"munna","current")
#way1 using dot operator
print(c1.BankName)
#print(c1.accno)
#print(c3.acctype)
c2.getcc()
c1.getcc()
c3.accno=896
c3.display()
