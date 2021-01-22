#program 54
#python program to demonstrate the single inheritence


class A:
    def view(a):
        print("Class A")
class B(A):
    def display(b):
        print("This is class B")

obja=A()
obja.view()
objb=B()
objb.display()
objb.view()
