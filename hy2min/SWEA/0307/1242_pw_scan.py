import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    hex_list = []
    for i in range(n):
        hexa = ''
        for j in range(m):
            if arr[i][j] != '0':
                hexa += arr[i][j]
            else:
                if hexa:
                    if hexa not in hex_list:
                        hex_list.append(hexa)
                    hexa = ''
    print(hex_list)
