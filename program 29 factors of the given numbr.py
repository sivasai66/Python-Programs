#30 Program to print the prime number of the given range
num = int(input("Enter the range"))

for i in range(0,num+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                 break
                    
            
        else:
           print(i)

      
                
   

    
    
    
    
