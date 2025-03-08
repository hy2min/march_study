arr = [input() for _ in range(4)]
print(f'긴문장:{arr.index(max(arr, key=len))}')
print(f'짧은문장:{arr.index(min(arr, key=len))}')