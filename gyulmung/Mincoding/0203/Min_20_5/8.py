lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
Result = []

def BBQ(n, m):
    global Result

    if n < len(lst1) and m < len(lst2):
        if lst1[n] >= lst2[m]:
            Result.append(lst2[m])
            BBQ(n, m + 1)

        elif lst1[n] <= lst2[m]:
            Result.append(lst1[n])
            BBQ(n + 1, m)
    elif n < len(lst1):
            for i in range(n, len(lst1)):
                Result.append(lst1[i])
    elif m < len(lst2):
            for i in range(m, len(lst2)):
                Result.append(lst2[i])

BBQ(0, 0)
print(*Result)