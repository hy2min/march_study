def inspect():
    score = 0
    for i in range(length-1):
        score = score_cal(i, score)
    return score

def score_cal(a, score):
    gap = ord(arr[a]) - ord(arr[a + 1])
    if gap == 0:
        score -= 50
    elif -5 <= gap <= 5:
        score += 3
    elif gap >= 20 or gap <= -20:
        score += 10
    return score

def dfs(level):
    global Max, cnt
    if level == n:
        Max = max(Max, inspect())
        return
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] == arr[j]: continue
            arr[i], arr[j] = arr[j], arr[i]
            dfs(level+1)
            arr[i], arr[j] = arr[j], arr[i]

arr = list(input())
length = len(arr)
n = int(input())
Max = -21e8
dfs(0)
print(Max)