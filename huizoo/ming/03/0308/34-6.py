n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
    arr[i] = (arr[i], 1)
cnt = 0
while arr:
    weight1, is_gold1 = arr.pop(0)
    weight2, is_gold2 = arr.pop(0)
    cnt += is_gold1 + is_gold2
    if is_gold1 and is_gold2:
        Max = 2*max(weight1, weight2)
        input_flag = 0
        for i in range(len(arr)):
            if Max < arr[i][0]:
                input_flag = 1
                arr.insert(i, (Max, 0))
        if not input_flag:
            arr.append((Max, 0))
    else:
        break
print(cnt)