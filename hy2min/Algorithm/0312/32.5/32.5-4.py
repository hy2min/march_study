def find_range(num, direction):
    global left, right
    if direction == 'DOWN':
        right = num - 1
    elif direction == 'UP':
        left = num + 1

    if left > right:
        return

    if left == right:
        return

left = 1
right = 50

n = int(input())


for _ in range(n):
    num, direction = input().split()
    num = int(num)
    find_range(num, direction)

if left > right:
    print('ERROR')
elif left == right:
    print(left)
else:
    print(str(left) + ' ~ ' + str(right))
