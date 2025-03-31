# 톱니개수 하드코딩
arr = [[3, 2, 5, 3],
       [7, 6, 1, 6],
       [4, 9, 2, 7]]

# 회전 수 입력 받기
lst = list(map(int, input().split()))
print(lst)

for i in range(len(lst)):
    for j in range(lst[i]):
        # 마지막 수를 stack에 담는다.
        stack = []
        stack.append(arr[2][i])
        # 각 자리를 아래로 한칸씩 내린다
        arr[2][i], arr[1][i] = arr[1][i], arr[0][i]
        # 첫번쨰에 stack의 수를 담는다.
        arr[0][i] = stack.pop()
        # 주어진 횟수만큼 반복한다.
for i in arr:
    print(*i, sep='')