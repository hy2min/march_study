
def where_gas(length, K, M, ai):
    go = 0
    count = 0
    for z in range(length, length + K + 1):  #K는 전역으로 입력
        for k in range(M):  # M 전역으로 입력
            if z == ai[k]:  # ai()전역으로 입력
                count += 1
                go = ai[k] - length
    return count, go





test_case = 1

for i in range(1,test_case+1):
    K, N, M = 3, 10, 5
    ai = [1, 3, 5, 7, 9]
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
        result = gas_charge
    print(f'#{i} {result}')