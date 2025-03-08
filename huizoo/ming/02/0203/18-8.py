train = [3,7,6,4,2,9,1,7]
team = list(map(int, input().split()))
start_index = train.index(team[0])
print(f'{start_index}번~{start_index+2}번 칸')
