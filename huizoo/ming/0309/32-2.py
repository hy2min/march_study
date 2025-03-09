n = int(input())
arr = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    arr.append((name, score, i))
    arr.sort(key=lambda x: (x[1], x[2]), reverse=True)
    for row in arr[:3]:
        print(row[0], end=' ')
    print()
