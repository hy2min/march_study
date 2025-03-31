up = list(map(int, input().split()))
down = list(map(int,  input().split()))
counting_teeth = [0]*10


for i in range(5):
    if up[i] == 1 and down[i] == 1:
        counting_teeth[i] += 1

count = 0
for i in range(5):
    if counting_teeth[i] >= 1:
        count += 1
print(f'{count}개')