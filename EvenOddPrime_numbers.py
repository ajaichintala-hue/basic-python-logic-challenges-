#printing 2 to 100 prime numbers, if it is not prime then print it as even or odd numbers using for loop

for i in range(2,101):
  n=i
  x=True
  for j in range(2,n):
    if n%j==0:
      x=False
      break
  if x:
    print(f"{n}-Prime ")
  elif(n%2==0):
    print(f"{n}-Even")
  else:
    print(f"{n}-Odd")

