import sys
sys.stdin = open("input.txt", "r")
T = 10

for tc in range(1, T + 1):
    N=int(input())
    boxes=list(map(int,input().split()))


    answer= 0

    for i in range(N):
        max_height = -21e8
        min_height = 21e8
        for j in range(len(boxes)):
            if min_height>boxes[j]:
                min_height = boxes[j]
                boxes[j] += 1

            if max_height < boxes[j]:
                max_height= boxes[j]
                boxes[j] -= 1

    if max_height-min_height>=0:
        answer=max_height-min_height

    print(f'#{tc} {answer}')