arr = list(map(int, input().split()))
n = int(input())
Max = 0

def dfs(lst, level, Sum):
    global Max
    if level == n:
        Max = max(Max, Sum)
        return
    for i in range(0, 3):
        lst2 = lst[:]
        if level >= 1:
            for idx in range(6):
                lst2[idx] *= 2
        temp1 = lst2[i]
        Sum += temp1
        lst2[i] = 0
        for j in range(3, 6):
            temp2 = lst2[j]
            Sum += temp2
            lst2[j] = 0
            for k in range(1, 5):
                temp3 = lst2[k]
                Sum += temp3
                lst2[k] = 0
                dfs(lst2, level+1, Sum)
                lst2[k] = temp3
                Sum -= temp3
            lst2[j] = temp2
            Sum -= temp2
        lst2[i] = temp1
        Sum -= temp1

dfs(arr, 0, 0)
print(Max)