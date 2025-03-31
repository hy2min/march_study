T = int(input())                        # testcase 개수
for test_case in range(1, T + 1):       # case별로 처리
    number = int(input())               # case별 입력 개수
    arr = [i for i in map(int,input().split())]
    Max = arr[0]                        # 가장 첫번째 값을 최대값으로 가정
    Min = arr[0]                        # 가장 첫번째 값을 최소값으로 가정
    for i in range(number):           
        if Max < arr[i]:
            Max = arr[i]
        if Min > arr[i]:
            Min = arr[i]
    print(f"#{test_case} {Max - Min}")