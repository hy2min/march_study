import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
end = arr[-1]
def abc():
    if N > 1:
        arr2 = list(map(int, sys.stdin.readline().split()))
        q = []
        q.append((0, arr2[0]))
        while q:
            now, through = q.pop()
            catch = arr[now] + through
            if catch >= end:
                return "권병장님, 중대장님이 찾으십니다"
            nxt, nxt_through = 0, 0
            Max = 0
            for i in range(now+1, N):
                if catch < arr[i]:
                    break
                if catch >= arr[i]:
                    if Max < arr[i] + arr2[i]:
                        Max = arr[i] + arr2[i]
                        nxt, nxt_through = i, arr2[i]
            if nxt:
                q.append((nxt, nxt_through))
        return "엄마 나 전역 늦어질 것 같아"
    else:
        return "권병장님, 중대장님이 찾으십니다"

ans = abc()
print(ans)