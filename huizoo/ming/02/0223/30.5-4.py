arr = [input() for _ in range(3)]
long = len(max(arr,key=len))
max_st = ''
for st in arr:
    if len(st) == long:
        max_st = max(max_st, st)
print(max_st)