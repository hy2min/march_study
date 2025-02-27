arr=[list(input())for _ in range(4)]


len_arr=[]

for i in arr:
    len_arr.append(len(i))

len_arr.sort()

print(*len_arr,end="")