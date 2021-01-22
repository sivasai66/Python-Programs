#program 42
#python script to demonstrate variable length arguments




def sum(*x):
    print(x)

sum(10,20,30)



def sum(*x):
    total=0
    for n in x:
        total=total+n
    print(total)
sum(10,20,3,5,6,4,5)
sum(10,20,3,5)
sum(3,5,6,4,5)
sum(10,20)
