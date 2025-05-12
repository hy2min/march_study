T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr= [list(input()) for _ in range(N)]
    Q=int(input())
    direct_arr = [
        [0, -1],
        [1, 0],
        [0, 1],
        [-1, 0],
    ]
    ans=[]
    for _ in range(Q):
        C,commands= input().split()

        now_x=0
        now_y=0
        f1=0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'X':
                    now_y = i
                    now_x = j
                    f1=1
                    break
            if f1:
                break

        next_y=0
        next_x=0
        flag=0
        direct=0

        for command in commands:
            if command == 'R':
                if direct == 3:
                    direct = 0
                else:
                    direct += 1
            if command == 'L':
                if direct == 0:
                    direct = 3
                else:
                    direct -= 1
            if command == 'A':
                next_x=now_x+direct_arr[direct][0]
                next_y=now_y+direct_arr[direct][1]

                if next_y > N-1 or next_y<0 or next_x>N-1 or next_x<0:continue
                if arr[next_y][next_x] == 'T':continue
                now_x=next_x
                now_y=next_y
        if arr[now_y][now_x] == 'Y':
            flag = 1

        ans.append(flag)

    print(f'#{tc}',end=" ")
    print(*ans)


