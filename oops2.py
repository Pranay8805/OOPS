class AadharCard:
    IssueAuth="IUDAI"#class variable
    def __init__(self,Ano,Name,DOB):#constructor-
    #construct an object/
    #gives info to the object/initilize an object
        self.Ano=Ano
        self.Name=Name
        self.DOB=DOB
    def getPassport(self):
        print(self.Name,"has got the passport")
    def display(self):
        print(self.Ano,self.Name,self.DOB)
A1=AadharCard(131,"prany","08-14-1995")
print(A1.Ano)
A1.getPassport()
A1.display()
print(A1.IssueAuth)

