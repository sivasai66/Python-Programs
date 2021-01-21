#15program to print a message "Advance Happy new year 2021" when number is divisible by 3

n=int(input("Enter the number"))
x=range(1,n+1)
for i in x:
    if(i%3==0):
        print("Advance Happy New year 2021")
    else:
        print(i)
