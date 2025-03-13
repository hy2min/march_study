T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort()
    weight = 0
    for i in range(M): # 트럭 수
        now = truck[i]
        now_weight = 0
        for j in range(len(container)): # 컨테이너 수 (내림차순 정렬)
            if now >= container[j]:
                now_weight = container.pop(j)
                break
        weight += now_weight
    print(f'#{tc} {weight}')

