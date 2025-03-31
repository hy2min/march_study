# 콜라츠 추측
import sys
input = sys.stdin.readline


N = int(input())
def abc(x, cnt):
    if x == 1:
        print(cnt)
        return

    if x % 2 == 0:
        abc(x//2, cnt+1)
    else:
        abc(x*3+1, cnt+1)

abc(N, 0)