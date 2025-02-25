# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    stop_list = []
    for i in range(P):
        a = int(input())
        stop_list.append(a)

    def Count_Bus_stop(num):

        count = 0
        for i in range(N):
            if arr[i][0] <= num <= arr[i][1]:
                count += 1
        return count

    lst = []
    for i in range(P):
        ans = Count_Bus_stop(stop_list[i])
        lst.append(ans)

    print(f"#{tc}",*lst)
