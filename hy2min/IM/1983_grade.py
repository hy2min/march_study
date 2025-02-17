grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']
T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    total_scores = [(i[0]*0.35 + i[1]*0.45 + i[2]*0.2) for i in scores]
    scores_sort = sorted(total_scores, reverse= True)
    student = scores_sort.index(total_scores[K-1])
    print(f'#{idx+1} {grade[student//(N//10)]}')
