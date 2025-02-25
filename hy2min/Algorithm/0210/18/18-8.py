train = [3,7,6,4,2,9,1,7]
team = list(map(int, input().split()))
part = [0] * 8
for student in team:
    if student in train:
        part[train.index(student)] = 1

start = -1
end = -1

for i in range(6):
    if part[i] == 1 and part[i+1] == 1 and part[i+2] == 1:
        start = i
        end = i + 2
        break
print(f'{start}번~{end}번 칸')