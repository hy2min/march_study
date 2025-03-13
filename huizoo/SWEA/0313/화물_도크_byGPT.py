# byGPT
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 종료 시간 기준 정렬
    arr.sort(key=lambda x: (x[1], x[0]))

    ed = 0
    cnt = 0

    for start, end in arr:  # 배열을 순차적으로 탐색하면서
        if start >= ed:  # 현재 배정된 회의의 종료 시간 이후라면
            cnt += 1  # 회의 배정
            ed = end  # 종료 시간 업데이트

    print(f'#{tc} {cnt}')