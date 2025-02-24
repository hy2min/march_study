arr = [list(map(int,input().split())) for _ in range(5)]

remove_one = [row for row in arr if row != [1]*4]
ans = [[0]*4] *(5-len(remove_one)) + remove_one

for i in ans:
    print(*i)