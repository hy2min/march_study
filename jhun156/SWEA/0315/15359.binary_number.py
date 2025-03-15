# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    a,b = input().split()
    N = int(a)
    arr = list(b)
    tmp = ''
    for i in range(N):
        ret1 = bin(int(arr[i], 16))   # 16진수를 10진수로 변환
        ret2 = ret1[2:]
        for j in range(4-len(ret2)):
            tmp += '0'
        tmp += ret2

    print(f"#{tc} {tmp}")