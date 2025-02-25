n = int(input())
y,x = 5,5
i = 0
arr = []
for i in range(n):
    a = input()
    arr.append(a)

for i in range(n):
    if arr[i] == 'up':
        y -= 1
    elif arr[i] == 'down':
        y += 1
    elif arr[i] == 'left':
        x -= 1
    elif arr[i] == 'right':
        x += 1
    else:
        print(f"{y},{x}")