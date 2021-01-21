#62 Python program to count number of instances created

class Student:
    count=0
    def __init__(s,name,age):
        s.name=name
        s.age=age
        Student.count=Student.count+1
    def display(s):
        print("Name: ", s.name, "Age :", s.age)

obj1=Student("Klu",44)
obj2=Student("Klef",454)
obj3=Student("Klh",4)
print("Total Number of objects created = ", Student.count)
              
