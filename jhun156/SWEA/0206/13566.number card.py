# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = list(map(int,input()))
    for i in range(N-1):
        for j in range(i+1,N):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    Max_value,Max = 0,0
    for i in range(N):
        count = 0
        for j in range(i,N):
            if lst[i] == lst[j]:
                count += 1
                if Max <= count:
                    Max = count
                    Max_value = lst[i]
            else:
                break
    print(f"#{test_case} {Max_value} {Max}")
