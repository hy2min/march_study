# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(T):
    arr = list(map(int,input().split()))
    test_case = arr.pop(0)
    cnt = 0

    def Line(arr):

        global cnt
        lst = arr[:]
        sorted_arr = sorted(arr)
        n = len(lst)
        while lst != sorted_arr:
            for i in range(n-1):
                if lst[i] > lst[-1]:
                    tmp = lst[-1]
                    for j in range(n-2,i-1,-1):
                        lst[j+1] = lst[j]
                        cnt += 1
                    lst[i] = tmp

        return lst

    for i in range(1,20):
        tmp_lst = Line(arr[:i+1])
        n = len(tmp_lst)
        for j in range(n):
            arr[j] = tmp_lst[j]

    print(test_case, cnt)