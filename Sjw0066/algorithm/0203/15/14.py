arr=[['P','O','T','I','O',0],['A','B','C','D','E',0],['Y','O','U','R','E',0]]

a,b= map(int,input().split())

for i in range(3):
   for j in range(a,b+1):
      print(arr[i][j],end="")