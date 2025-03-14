T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])
    student = [0]*N
    time = 0
    cnt = 0
    while cnt < N:
        room = [0] * 401
        time += 1
        for i in range(N):
            if student[i]: continue
            start, end = arr[i]
            if room[start] or room[end]: continue

            cnt += 1
            student[i] = 1
            if start < end:
                if end % 2 == 0:
                    for j in range(start, end+1):
                        room[j] = 1
                else:
                    for j in range(start, end+2):
                        room[j] = 1
            else:
                if start % 2 == 0:
                    for j in range(end, start+1):
                        room[j] = 1
                else:
                    for j in range(end, start+2):
                        room[j] = 1

    print(f'#{tc} {time}')