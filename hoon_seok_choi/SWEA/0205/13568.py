T = int(input()) #TC 개수

for tc in range(1, T+1) : #케이스 별로 처리
    N, M = map(int,input().split()) #케이스 별 입력 개수
    arr = list(map(int, input().split()))


    #이웃한 M개 합 계산을 위한 반복범위 지정
    sum_arr = []
    sum_unit = 0

    for i in range(N-M+1) :
        for j in range(M) :
            sum_unit += arr[i+j]
        sum_arr.append(sum_unit)
        sum_unit = 0

    # 합 리스트 중 최대/최소값 계산
    max_v = max(sum_arr)
    min_v = min(sum_arr)

    print(f'#{tc} {max_v-min_v}')

