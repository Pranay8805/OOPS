class student:
    rno=123
    name="abc"
    branch="cse"
    def read(self):
        print("reading")
abc.read() 
               
abc=student()
print("rno",abc.rno)
print("name",abc.name)
print("branch",abc.branch)
