# import sys
# sys.stdin = open("input.txt","r")

T = 10
for i in range(1,T+1):
    test_case = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    y,x = 99, arr[99].index(2)
    # 시작점부터 시작하는게 아니라 도착지부터 위로 올라가는 방법
    # 다른 사람들 코드를 보고 해당 방법만 참고함

    while y > 0:
        if x > 0 and arr[y][x-1] == 1:
            while x > 0 and arr[y][x-1] == 1:
                x -= 1
                # 한번 왼쪽 이동했으니 이동경로를 살피고 왼쪽으로 최대한 이동
                # 한번 왼쪽으로 이동하면 왼쪽 끝까지 이동하거나 위로 올라가는 것 밖에 없음
                # 왼쪽 이동의 경우 ㅗ 모양을 만나면 위로 가야하는 것 아닌가 싶을수있는데
                # 사다리를 아래에서 위로 출발지를 찾을땐 왼쪽으로 끝까지 이동해야함
            y -= 1
        elif x < 99 and arr[y][x+1] == 1:
            while x < 99 and arr[y][x+1] == 1:
                x += 1
                # 마찬가지로 한번 오른쪽으로 이동하면 막힐때까지 오른쪽으로 가거나 위로 이동
            y -= 1
        else:
            y -= 1
            # 왼쪽, 오른쪽이 다 막혔다면 위로 올라가면 됨


    print(f"#{test_case} {x}")

