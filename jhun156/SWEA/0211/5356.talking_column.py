# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    word_list = []
    for i in range(5):
        string = list(input())
        word_list.append(string)
    Max = 0
    for i in range(5):
        if len(word_list[i]) > Max:
            Max = len(word_list[i])
    lst = [[0] * Max for _ in range(5)]
    # 0으로 초기화된 2차원 리스트
    for i in range(5):
        for j in range(len(word_list[i])):
            lst[i][j] = word_list[i][j]
    ans = ''
    for i in range(Max):
        for j in range(5):
            if lst[j][i] != 0:
                ans += lst[j][i]

    print(f"#{tc} {ans}")