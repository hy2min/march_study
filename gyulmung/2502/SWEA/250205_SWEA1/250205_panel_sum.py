def find_case(N, M, ai):
    arr = []
    counting = 0
    for i in range(N - M + 1):
        count = 0
        if counting < N - M + 1:
            for j in range(M):
            
                count += ai[counting + j]
            counting += 1
        arr.append(count)
    # print(arr)
    max_num = 0
    for i in range(len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
    

    min_num = arr[0]
    for i in range(len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]

    return max_num - min_num

test_case = int(input())

for i in range(1,test_case+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    result = find_case(N, M, ai)

    print(f'#{i} {result}')

