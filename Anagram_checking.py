str1=input("Enter the first  string: ")
str2=input("Enter the second string: ")
list1=sorted(str1.lower())
list2=sorted(str2.lower())
if list1==list2:
  print("Anagram")
else:
  print("Not an anagram")
