test_case = 1

for i in range(1, test_case + 1):
    N = int(input())
    Hight = list(map(int, input().split()))
    result = View(N, Hight)


    print(f'#{i} {result}')

def View(N, M):
    View_river = 0
    for i in range(2, N-1):
        arr = []
        for j in range(i -2 , i + 3):
            if j >= 10:
                if M[i] > M[j-2]:
                    arr.append(M[i] - M[j])
            else:
                if M[i] > M[j]:
                    arr.append(M[i] - M[j])
        print(arr)
        print(arr[0])
        Min_num = arr[0]
        print(Min_num)
        for k in arr:
            if Min_num > k:
                Min_num = k
        View_river += Min_num
    return View_river
        
test_case = 1