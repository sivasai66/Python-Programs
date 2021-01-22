#25 Program to check given number is prime or not
n= int(input("Enter the number"))
if(n>1):
    for i in range(2,n):
        if((n%i)==0):
            print("The given number is not a prime number")
            break;

    else:
        print("is a prime number")
       

else:
    print("not a prime ");
            

