string=input()
list1=[]
list1.append(string[0])
for i in range(len(string)):
  if string[i] not in list1:
    print(string[i], end=" ")
    list1.append(string[i])
  else:
    continue
