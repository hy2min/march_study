arr = [list(map(len,input())) for _ in range(4)]

M = arr.index(max(arr))
m = arr.index(min(arr))
print(f"긴문장:{M}")
print(f"짧은문장:{m}")
