string=input()
list1=[]
for s in range(len(string)):
  count=0
  if string[s] in list1:
    continue 
  else:
    for i in range(s,len(string)):
      if string[s]==string[i]:
        count+=1
        list1.append(string[i])
    print(string[s],count)

