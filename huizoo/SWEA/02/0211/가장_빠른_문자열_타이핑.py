T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    print(f'#{tc} {len(A)-(A.count(B)*(len(B)-1))}')