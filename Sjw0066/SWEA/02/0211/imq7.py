T= int(input())

for tc in range(1, T + 1):
    N ,K = map(int,input().split())
    score=[list(map(int,input().split())) for _ in range(N)]
    grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    final_score=[]

    for i in range(N):
        total_score=score[i][0]*0.35+score[i][1]*0.45+score[i][2]*0.2
        final_score.append(total_score)

    target=final_score[K-1]

    final_score.sort(reverse=True)
    rank=0

    for i in range(N):
        if target == final_score[i]:
            rank=i+1



    answer = grade[((rank-1) // (N // 10))]



    print(f'#{tc} {answer}')
