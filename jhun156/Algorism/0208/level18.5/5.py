arr = "ATKPTCABC"
rev_arr = ""
for i in range(len(arr)):
    rev_arr += arr[len(arr)-i-1]
a,b = input().split()

ans1 = arr.find(a)
ans2 = rev_arr.find(b)
result = (len(arr))-1-ans2-ans1
print(result)
