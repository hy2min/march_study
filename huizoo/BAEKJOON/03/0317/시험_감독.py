import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in A:
    if i <= B:
        cnt += 1
    else:
        remain = i-B
        if remain % C == 0:
            cnt += remain//C + 1
        else:
            cnt += remain//C + 2

print(cnt)