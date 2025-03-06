import sys
input = lambda : sys.stdin.readline()

N=int(input())
loc=list(map(int,input().split()))
power=list(map(int,input().split()))

flag=0
max_power=0

for i in range(N-1):
    if max_power>=loc[i]:
        if max_power < loc[i] + power[i]:
            max_power = loc[i] + power[i]

if max_power>=loc[N-1]:flag=1

if flag:
    print('권병장님, 중대장님이 찾으십니다')
else:
    print('엄마 나 전역 늦어질 것 같아')
