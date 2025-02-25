string = input()
n = int(input())

idx = list(string)
idx.remove(idx[n])

print("".join(idx))