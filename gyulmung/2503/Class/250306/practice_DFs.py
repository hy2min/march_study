# def dfs(level, Sum):
#     global cnt
#     if level == N:
#         if Sum == 10:
#             cnt += 1
#         return
#
#     for i in range(1, 5):
#         dfs(level + 1, Sum + i)
#
#
#
#
# N = int(input())
# dfs(0,0) # level Sum
# print(cnt)

# 내가 사용하는 수가 배수의 관계이면 그리디로 문제를 풀 수 있음
# 그리디란 뒤는 생각 안하고 앞에 있는 것으로 확인하며 풀어나가는 알고리즘이다.

# 거스름 돈을 줄 때 동전의 최소 개수
# N 값 입력(돈)
# 돈은 110원, 70원, 10원 있음

N = int(input())
coin = [110, 70, 10]
Min = 1e8

def dfs(money, cnt):
    global Min
    if money > N or cnt > Min:
        return
    if money == N:
        Min = min(cnt, Min)
        return

    for i in range(3):
        dfs(money + coin[i], cnt+1)

dfs(0, 0)
print(Min)