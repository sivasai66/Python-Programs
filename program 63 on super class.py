#63 python program to demonstrate super() method

class College():
    def __init__(self,id,cname,location):
        self.id=id
        self.cname=cname
        self.location=location
class Department(College):
    def __init__(self,id,cname,location,dname):
         super(). __init__ (id,cname,location)
         self.dname=dname
cse=Department(101,"klu","Vijayawada","Cse");
print(cse.id,cse.cname,cse.location,cse.dname)
       
        
