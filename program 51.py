#program 52
#python script to demonstrate class and object using __init__  method

class Employee:
    def __init__ (e,id,name):
        e.id=id
        e.name=name
    def display(e):
        print("Employee id :",e.id,"Employee Name: ",e.name)
emp = Employee(100,"Sivasai")
emp.display()
