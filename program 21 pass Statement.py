#21 Program to demonstrate the pass Statement

n = int(input("Enter the range"))
for i in range (0,n+1):
    if i%2==0:
        pass
    else:
        print(i)
