arr = [input() for _ in range(4)]
long = max(arr, key = lambda x : len(x))
short = min(arr, key = lambda x : len(x))

print(f'긴문장:{arr.index(long)}')
print(f'짧은문장:{arr.index(short)}')