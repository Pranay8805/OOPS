class student:
    rno=1234
    name="qwer"
    branch="etc"
    def read(self):
        rno=256
        print("rollno",rno)
        print("reading....")
    def write(self):
         print("writing....")
         
qwer=student()
print("rno",qwer.rno)
print("name",qwer.name)
print("branch",qwer.branch)
qwer.read()
qwer.write()
         


#comment


class student:
    rno=123
    branch="etc"
    name="abc"
    def read(self):
        print("reading......")
    def write(self):
        print("writing.....")
abc=student()
print("rno",abc.rno)
print("branch",abc.branch)
print("name",abc.name)
abc.read()
abc.write()
    