arr = [input() for _ in range(4)]
arr.sort(key=len)
print(*arr,sep='\n')