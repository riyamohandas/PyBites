n=int(input("Enter the number to reverse: "))
reversed=0
while n!=0:
  digit=n%10
  reversed=(reversed*10)+digit
  n//=10
print(reversed)
