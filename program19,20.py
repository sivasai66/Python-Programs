#19 Program to demostrate break statement
n=int(input("Enter the Range"))
for i in range(1,n+1):
    if(i==5):
        break
    elif(i==4):
        continue
    else:
        print (i)
