N = int(input())
arr = [input() for _ in range(N)]
arr.sort(key = lambda x: (len(x),x))
print('\n'.join(arr))