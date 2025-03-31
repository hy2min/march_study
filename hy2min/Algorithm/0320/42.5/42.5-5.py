def backtracking(level, score):
    global max_score


    if level == n:
        if max_score < score:
            max_score = score
        return

    for i in range(len(arr)-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]

        new_score = score
        if arr[i] == arr[i+1]:
            new_score -= 50
        elif abs(ord(arr[i]) - ord(arr[i+1])) <= 5:
            new_score += 3
        elif abs(ord(arr[i]) - ord(arr[i+1])) >= 20:
            new_score += 10

        backtracking(level+1, new_score)

        arr[i], arr[i+1] = arr[i+1], arr[i]



arr = list(input())
n = int(input())
max_score = -21e8

initial_score = 0
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        initial_score -= 50
    elif abs(ord(arr[i]) - ord(arr[i + 1])) <= 5:
        initial_score += 3
    elif abs(ord(arr[i]) - ord(arr[i + 1])) >= 20:
        initial_score += 10
backtracking(0, initial_score)
print(max_score)