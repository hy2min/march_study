T = int(input())
for tc in range(1, T+1) : 
    N, K = map(int, input().split())
    student = [list(map(int, input().split())) for _ in range(N)]
    n = int(N//10)
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N) : 
        student[i][0] *= 35
        student[i][1] *= 45
        student[i][2] *= 20
        student[i] = sum(student[i])
    
    temp = student[K-1]
    student.sort()
    student_score = student.index(temp) // n

    print(f'#{tc} {score[-student_score-1]}')