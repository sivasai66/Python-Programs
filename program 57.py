#program 58
#python program to demonstrate the hierachal inheritence


class A:
    def view(a):
        print("Class A")
class B(A):
    def display(b):
        print("This is class B")
class C(A):
    def show(c):
        print("You are in class C")

obja=A()

objb=B()

objc=C()
obja.view()
objb.display()
objc.show()
objb.view()
objc.view()
