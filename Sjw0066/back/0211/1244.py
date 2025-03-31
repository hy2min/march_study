N = int(input())
switches = list(map(int, input().split()))
M = int(input())
lst = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    if lst[i][0] == 1:
        power = 1
        while 1:
            index = (lst[i][1] * power) - 1
            if index > len(switches) - 1:
                break
            switches[index] = 1 - switches[index]
            power += 1
    else:
        width = 1
        while 1:
            right = lst[i][1] + width - 1
            left = lst[i][1] - width - 1

            if right > len(switches) - 1 or left < 0:
                break

            if switches[right] == switches[left]:
                switches[right] = 1 - switches[right]
                switches[left] = 1 - switches[left]

            if switches[right] != switches[left]:
                break
            width += 1
        switches[lst[i][1] - 1] = 1 - switches[lst[i][1] - 1]

while switches:
    for i in range(20):
        try:
            print(switches.pop(0), end=" ")
        except:
            break
    print()
