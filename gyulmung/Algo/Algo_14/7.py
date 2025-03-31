numbers = list(map(int, input().split()))

numbers = sorted(numbers, reverse = True)
print(*numbers, sep = "")