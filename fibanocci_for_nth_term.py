n=int(input("Enter the nth number : "))
a,b=0,1
for i in range(n):
  print(b, end=" ")
  a, b = b, a + b
