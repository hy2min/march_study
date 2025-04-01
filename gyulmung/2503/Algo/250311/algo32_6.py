import sys
sys.stdin =open('input.txt','r')

# 다인이 도움 받음
N, M = map(int, input().split())
member = [[0,[]] for _ in range(N)]

for i in range(M):
    num, name = input().split()
    member[int(num)][0] += 1
    member[int(num)][1].append(name)

ret = sorted(member, key=lambda x:x, reverse=True)
print(*ret[0][1])

# 정원이 도움 받음(dictionary로 풀기)