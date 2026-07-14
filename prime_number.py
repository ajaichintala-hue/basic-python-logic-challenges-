#prime numbers below 100 using while and for loop
for i in range(2,100):
    n=i
    x=True
    j=2
    while j<n:
        if(n%j==0):
            x=False
           break
         j=j+1
    if(x):
         print(n,end=",")
    
   
