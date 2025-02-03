arr=[[0]*8 for _ in range(2)]

for i in range(2):
   str1=list(input())
   for j in range(len(str1)):
      arr[i][j] = str1[j]

cnt=0
for i in range(8):
   if arr[0][i] != 0 or arr[1][i] != 0:
      if arr[0][i] != arr[1][i] :
         cnt += 1 

print(cnt)