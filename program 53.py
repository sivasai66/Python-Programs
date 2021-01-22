#program 54
#python script to demonstrate parameterized constructor

class Employee:
    def __init__ (e,id,name):
        print("Parameterized Constructer")
        print(name,"-",id)
emp=Employee(19,"Covid")
        
