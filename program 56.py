#program 57
#python program to demonstrate the multiple inheritence


class A:
    def view(a):
        print("Class A")
class B:
    def display(b):
        print("This is class B")
class C(A,B):
    def show(c):
        print("You are in class C")

obja=A()
obja.view()
objb=B()
objb.display()
objc=C()
objc.show()
objc.display()
objc.view()
