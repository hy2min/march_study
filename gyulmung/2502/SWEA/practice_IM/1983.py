import sys # 1시간
sys.stdin = open('input.txt', 'r')

T = int(input())

for test in range(1, T + 1):
    N, M = map(int, input().split())
    record = [list(map(int, input().split())) for _ in range(N)]

    rank_record = []
    # 성적의 총점 구하고 정렬
    for i in range(N):
        total_record = record[i][0] * 0.35 + record[i][1] * 0.45 + record[i][2] * 0.2
        rank_record.append(total_record)
        rank_record_student = sorted(rank_record)

    # 성적의 커트라인 정하기
    rank_people = N // 10
    rank_cutline = []
    for i in range(0, len(record), rank_people):
        rank_cutline.append(rank_record_student[i])

    # 성적확인하기
    ranking = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0']
    search_rank = rank_record[M-1]
    for i in range(0,9):
        if rank_cutline[i] <= search_rank < rank_cutline[i+1]:
            print(f'#{test} {ranking[i]}')
        elif search_rank >= rank_cutline[9]:
            print(f'#{test} {"A+"}')
