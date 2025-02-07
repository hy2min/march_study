# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    number = list(map(int,input()))
    answer = []
    for i in range(N):
        count = 1
        if number[i] == 1:
            for j in range(i+1,N):
                if number[i] == number[j]:
                    count += 1
                else:
                    break
            answer.append(count)
    for i in range(len(answer)-1):
        for j in range(i+1,len(answer)):
            if answer[i] > answer[j]:
                answer[i],answer[j] = answer[j], answer[i]
    result = answer[len(answer)-1]
    print(f"#{test_case} {result}")
