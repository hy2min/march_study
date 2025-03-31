def cal(a, b, op):
    if op == '!!':
        ret = (a-b) * (a+b)
    elif op == '#':
        ret = max(a, b)
    elif op == '$':
        ret = a**2 - b**2
    elif op == '&':
        ret = (a+b) ** 2
    return ret

def backtracking(idx, result):
    global cnt
    if idx == len(numbers)-1:
        if result == 100:
            cnt += 1
        return

    for op in ['!!', '#', '$', '&']:
        new_result = cal(result, numbers[idx+1], op)
        backtracking(idx + 1, new_result)


n = int(input())
numbers = list(map(int, input().split()))
cnt = 0
backtracking(0, numbers[0])

print(cnt)
