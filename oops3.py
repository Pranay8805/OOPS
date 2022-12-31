class edyoda:
    companyname="edyoda"#Class Variable
    def __init__(self,tno,tname,tstream):#constructor- construct an object/
#give info to the objects/initialize an object
        self.tno=tno
        self.tname=tname
        self.tstream=tstream
    def getbatch(self):
        #All instance variables/methods need self for referance
        print(self.tname,"has got the batch")
    def display(self):
        print(self.tno,self.tname,self.tstream)
t1=edyoda(34,"sagar","python")
t1.display()

print(t1.tname)
t1.getbatch()