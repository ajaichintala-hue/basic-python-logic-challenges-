#reverse of the number using while loop

n=int(input("Enter any number :"))
rev=0
while n!=0:
    ld=n%10  #ld=last digit
    rev=rev*10+ld
    n=n//10
print(rev)
