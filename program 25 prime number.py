#26 Program to check given number is armstrong or not
n= int(input("Enter the number"))
sum=0
temp=n
while temp > 0:
    digit=temp%10
    sum = sum+(digit*digit*digit);
    temp = temp/10



if(n==sum):
    print("Armstrong number")
else:
    print("not an armstrong")
