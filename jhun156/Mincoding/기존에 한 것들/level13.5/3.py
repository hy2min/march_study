A = [i for i in map(int,input().split())]
B = [i for i in map(int,input().split())]
C = [i for i in map(int,input().split())]

arr = []

for i in range(5):
    arr.append(A[i]*B[i]+C[i])

print(*arr)