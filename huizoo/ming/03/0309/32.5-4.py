n = int(input())
left = 0
right = 50
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'DOWN':
        right = min(a, right)
    elif b == 'UP':
        left = max(a, left)
if right - left == 2:
    print(left+1)
elif right - left > 2:
    print(f'{left+1} ~ {right-1}')
else:
    print("ERROR")