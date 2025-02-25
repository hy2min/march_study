train = [3,7,6,4,2,9,1,7]
team = [i for i in map(int,input().split())]

for i in range(6):
    for j in range(3):
        if train[i+j] == team[j]:
            print(f"{i}번~{i+2}번 칸")
            break