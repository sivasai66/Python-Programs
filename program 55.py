#program 56
#python program to demonstrate the multiple inheritence


class A:
    def view(a):
        print("Class A")
class B(A):
    def display(b):
        print("This is class B")
class C(B):
    def show(c):
        print("You are in class C")

obja=A()
obja.view()
objb=B()
objb.display()
objb.view()
objc=C()
objc.show()
objc.display()
objc.view()
