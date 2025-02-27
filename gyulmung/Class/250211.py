# 동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.
#
# i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
# 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
#
# [입력]
# 첫 줄에 게임의 개수 T, 다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, 다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
# (1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)
#
# [출력]
# #과 게임번호, 빈칸에 이어 빈칸으로 구분된 돌의 상태를 출력한다.
import sys
sys.stdin = open('input.txt', 'r')


t = int(input())

def find_stone(y, x, arr):
    for i in range(1, x + 1):
        if y - i < 0 or y + i > N -1:
            continue
        elif arr[y-i] == 1 and arr[y + i] == 1:
            arr[y - i], arr[y + i] = 0, 0
        elif arr[y-i] == 0 and arr[y + i] == 0:
            arr[y - i], arr[y + i] = 1, 1
    return arr


for i in range(1, t + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for j in range(M):
        re_i, re_j = map(int, input().split())
        reverse_arr = find_stone(re_i - 1, re_j, arr)
    print(reverse_arr)