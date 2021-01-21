#14program to print even number in the given range

n=int(input("Enter the Range"))
x=range(1,n+1)
for i in x:
    if(i%2==1):
        print(i)
