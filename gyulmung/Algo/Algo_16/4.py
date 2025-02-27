A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = []

for i in range(4):
    result.append(A[i] + B[3-i])
    print(result[i], end = " ")