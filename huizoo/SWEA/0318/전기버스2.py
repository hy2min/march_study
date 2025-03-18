import heapq

def abc():
    heap = [(0, 0+arr[0], 0, arr[0])]
    while heap:
        # 현재 교환횟수, 인덱스와 갈 수 있는 거리 합, 현재 인덱스, 충전지로 갈 수 있는 거리
        # Sum 은 값을 사용하진 않지만 힙의 특성을 이용하기 위해 사용
        cnt, Sum, idx, drive = heapq.heappop(heap)
        for i in range(1, drive+1):
            if idx+i+arr[idx+i] >= n:
                return cnt+1
            heapq.heappush(heap, (cnt+1, -(idx+i+arr[idx+i]), idx+i, arr[idx+i]))

    return cnt

T = int(input())
for tc in range(1, T+1):
    n, *arr = list(map(int, input().split()))
    n -= 1
    print(f'#{tc} {abc()}')