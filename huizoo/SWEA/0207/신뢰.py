T = int(input())
for tc in range(1, T+1) :
    N, *arr = input().split()
    arr_O, time_O = [], 0
    arr_B, time_B = [], 0

    # 짝수 인덱스 탐색
    for i in range(0, 2*int(N), 2) :
        if arr[i] == 'O' :
            arr_O.append(int(arr[i+1]))
            # cnt_O += 1
        elif arr[i] == 'B' :
            arr_B.append(int(arr[i+1]))
            # cnt_B += 1
    # # 이동거리 축적
    # for i in range(cnt_O - 1) :
    #     time_O += abs(arr_O[i] - arr_O[i + 1])
    # for i in range(cnt_B - 1) :
    #     time_B += abs(arr_B[i] - arr_B[i + 1])
    len_arr_O = len(arr_O)
    len_arr_B = len(arr_B)
    max_len = max(len_arr_O, len_arr_B) - 1
    i = 0
    # 시작할때 이동거리가 계산이 안되어 있으므로 직접 추가(비어있을 경우 오류 방지 위해 if문 사용)
    if arr_O:
        time_O += arr_O[0]
    if arr_B:
        time_B += arr_B[0]
    while i <  max_len :
        if arr_O and i <= len(arr_O) :
            if time_O == time_B:
                time_O += 1
            time_O += abs(arr_O[i] - arr_O[i + 1]) + 1
        if arr_B and i <= len(arr_O) :
            time_B += abs(arr_B[i] - arr_B[i + 1]) + 1
        i += 1

    # # 같은 위치에 버튼이 있으면 기다려야하기 때문에 1 씩 증가
    # for button in arr_O :
    #     if button in arr_B :
    #         cnt_O += 1
    #         cnt_B += 1
    print(f'#{tc} {max(time_O, time_B)}')