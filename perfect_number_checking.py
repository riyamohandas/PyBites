n=int(input("Enter the number : "))
sum=0
temp=n
for i in range(1,n):
  if n%i==0:
    sum+=i
if sum==temp:
  print("perfect")
else:
  print("not perfect")
