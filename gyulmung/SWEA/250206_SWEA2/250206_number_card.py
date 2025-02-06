import sys
sys.stdin = open('input.txt','r')

def where_gas(length, K, M, ai):
    go = 0
    count = 0
    for z in range(length, length + K + 1):  #K는 전역으로 입력
        for k in range(M):  # M 전역으로 입력

            if length <N and z == ai[k]:  # ai()전역으로 입력
                count += 1
                go = ai[k] - length
    return count, go




test_case = int(input())

for i in range(1,test_case+1):
    K, N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    gas_charge = 0
    length = 1
    for j in range(M):
        gas_count, go_length = where_gas(length, K, M, ai)
        if length >= N:  # 종점 개수
            break
        elif length < N and gas_count >= 1:
            length = length + go_length
            gas_charge += 1
        else:
            result = 0
        result = gas_charge - 1
    print(f'#{i} {result}')