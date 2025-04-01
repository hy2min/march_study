import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test in range(1, T+1):
    n, arr = input().split()
    arr = '0x'+arr
    a = bin(int(arr, 16))[2:]
    if len(a) % 4 != 0:
        a = '0' * (4 - len(a) % 4) + a
    print(f'#{test} {a}')

# t=int(input())
# for tc in range(1,t+1):
#     n,arr=input().split()
#     ans=bin(int(arr,16))[2:]
#     print(f'#{tc} {"0"*(4*int(n)-len(ans))+ans}')
