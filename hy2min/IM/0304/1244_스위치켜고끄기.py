sw = int(input())
arr = [0] + list(map(int,input().split()))
n = int(input())
for _ in range(n):
    s, idx = map(int, input().split())
    if s == 1:
        for i in range(idx,sw+1,idx):
            arr[i] = 1-arr[i]
    elif s == 2:
        left = right = idx

        while left > 1 and right <= sw and arr[left-1] == arr[right + 1]:
            left -= 1
            right += 1

        for i in range(left, right+1): 
            arr[i] = 1- arr[i]
arr = arr[1:]

for i in range(0,sw,20):
    print(*arr[i:i+20])