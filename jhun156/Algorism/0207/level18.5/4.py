up = [i for i in map(int,input().split())]
down = [i for i in map(int,input().split())]
ans = 0
for i in range(5):
    if up[i] == down[i] == 1:
        ans += 1
print(f"{ans}개")