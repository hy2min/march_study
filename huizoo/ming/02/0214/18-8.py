train = [3,7,6,4,2,9,1,7]
team = list(map(int, input().split()))
for i in range(6):
    if train[i:i+3] == team:
        print(f'{i}번~{i+2}번 칸')
        