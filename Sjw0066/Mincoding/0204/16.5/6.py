str1=input()

lst1=list(str1)
lst2=sorted(lst1)


minindex=lst1.index(lst2[0])
maxindex=lst1.index(lst2[len(lst2)-1])

print(maxindex)
print(minindex)