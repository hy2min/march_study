num = list(map(int,input().split()))
command = input()
for i in command:
    if i =='m':
        min_idx = num.index(min(num))
        print(num.pop(min_idx),end="")
    if i == 'x':
        max_idx = num.index(max(num))
        print(num.pop(max_idx),end="")

