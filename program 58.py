#program 59
#python program to demonstrate the hybrid inheritence


class A:
    def view(a):
        print("Class A")
class B(A):
    def display(b):
        print("This is class B")
class C(B):
    def show(c):
        print("You are in class C")

class D(B,A):
    def show1(d):
        print("WE are in the D class")

        
obja=A()

objb=B()

objc=C()

objd=D()

obja.view()
objb.display()
objc.show()
objd.show1()


objb.view()
objc.show()

objd.view()
objd.display()

objc.view()


