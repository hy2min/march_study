import sys
sys.stdin = open('input.txt','r')

def where_gas(length, K, M, ai):
    count = 0
    for z in range(length + 1, length + K + 1):  #K는 전역으로 입력
        for k in range(M):  # M 전역으로 입력
            if z >= N:
                length = z
                break
            elif z < N and z == ai[k]:  # ai()전역으로 입력
                count += 1
                length = ai[k]
    return count, length

test_case = int(input())

for i in range(1,test_case+1):
    K, N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    gas_charge = 0
    length = 1
    for j in range(M):
        gas_count, length = where_gas(length, K, M, ai)
        if length >= N:  # 종점 개수
            break
        elif length < N and gas_count >= 1:
            gas_charge += 1
        elif gas_count < 1:
            gas_charge = 0
            break
    result = gas_charge
    print(f'#{i} {result}')