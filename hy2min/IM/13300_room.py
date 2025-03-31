
n, k = map(int,input().split()) # 학생 수, 방 배정 최대 인원 수
student = [[0]*7 for _ in range(2)]

for _ in range(n): # 성별, 학년
    s, y = map(int,input().split())
    student[s][y] += 1

cnt = 0
for i in student:
    for j in i:
        cnt += (j+k-1) //k
print(cnt)