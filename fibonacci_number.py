#code for fibonacci of numbers using for looop and functons

def fibonacci(n):
  a=0
  b=1
  for n in range(n):
    c=a+b
    a=b
    b=c
  print(c)
  return c
s=int(input("Enter your fib digit :"))
fibonacci(s)


