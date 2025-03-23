teeth = list(map(int, input().split()))
tooth = list(map(int, input().split()))
cnt = 0
for i in range(5):
    if teeth[i] and tooth[i]:
        cnt += 1
print(f'{cnt}개')