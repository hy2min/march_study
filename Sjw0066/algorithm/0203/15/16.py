a= input()

arr=[[0]*3 for _ in range(3)]

ord_index=ord(a)

for i in range(2,-1,-1):
    for j in range(3-i):
         arr[i][j] = chr(ord_index)
         ord_index += 1

for i in arr:
   for j in i :
      if j==0 :
         print("",end="")
      else:
         print(j,end="")
   print()  