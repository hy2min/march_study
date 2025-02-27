arr=[['D','A','T','A','W',0],['B','B','Q','K',0,0]]

a=int(input())

if a%2==0:
   arr[1]=list(sorted(filter(bool,arr[1])))
else:
   arr[0]=list(sorted(filter(bool,arr[0])))

for i in arr:
   for j in i :
      if j==0 :
         print("",end="")
      else:
         print(j,end="")
   print()   





