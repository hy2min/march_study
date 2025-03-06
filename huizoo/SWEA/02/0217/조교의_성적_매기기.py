t = int(input())
for tc in range(1, t+1):
    hakjeom = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())
    K -= 1
    score = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        score.append(a*35+b*45+c*20)
    student = score[K]
    score.sort(reverse=True)
    Rank = score.index(student)
    Rank = (Rank//(N//10))
    print(f'#{tc} {hakjeom[Rank]}')