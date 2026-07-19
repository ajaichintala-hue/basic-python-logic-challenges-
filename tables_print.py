#printing the tables we want using for loop in functions

def table_printing(n):
  k=n
  for i in range(1,11):
    print(f"{k}*{i}={k*i}")
s=int(input("Enter any number : "))
table_printing(s)
