p = int(input())
for _ in range(p):
    arr = list(map(int, input().split()))

    tc = arr[0]
    student = arr[1:]

    cnt = 0
    for i in range(1, len(student)):
        for j in range(0,i):
            if student[i] < student[j]:
                cnt += 1
    print(f'{tc} {cnt}')