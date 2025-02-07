# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input().split()))
    Max = 0
    for i in range(N):
        count = 0      #리스트의 자신의 오른쪽에 자신보다 작은 개수 세기
        for j in range(i+1,N):
            if lst[i] > lst[j]:
                count += 1
        if Max < count:
            Max = count
            
    print(f"#{test_case} {Max}")