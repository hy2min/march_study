arr = [0] * 6

a,b,c = map(int,input().split())

arr[int(a)] = 1
arr[int(b)] = 1
arr[int(c)] = 1

print(*arr)