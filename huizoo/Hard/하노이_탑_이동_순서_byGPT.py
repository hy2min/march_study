def hanoi(n, start, mid, end):
    if n == 1:
        # 기저 사례: 원판 1개를 바로 옮김
        print(start, end)
    else:
        # 1단계: n-1개를 출발에서 보조로 옮김 (목표 기둥을 임시로 사용)
        hanoi(n-1, start, end, mid)
        # 2단계: 가장 큰 원판을 출발에서 목표로 옮김
        print(start, end)
        # 3단계: n-1개를 보조에서 목표로 옮김 (출발 기둥을 임시로 사용)
        hanoi(n-1, mid, start, end)

n = int(input())
# 총 이동 횟수: 2^n - 1
print(2**n - 1)
hanoi(n, 1, 2, 3)
