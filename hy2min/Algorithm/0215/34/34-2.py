battery = input()
def capacity(battery):
    start, end = 0, 9
    while start <= end:
        mid = (start + end) // 2

        if battery[mid] == "#":
            start = mid + 1
        else:
            end = mid - 1
    return start

result = capacity(battery)
print(f'{result*10}%')
