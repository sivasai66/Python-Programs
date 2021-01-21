#60 python program to demonstrate Polymorphism (method Overloading)

class Shape:
    def area(s,a=None,b=None):
        if a!=None and b!=None:
            print("Area:",a*b)
        elif a!=None:
            print("Area : ",a*a)

        else:
            print("Area : ",0)
s=Shape()
s.area()
s.area(5)
s.area(5,10)
