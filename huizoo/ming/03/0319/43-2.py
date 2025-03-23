dic = {
    "POP": "yes",
    "TOM": "yes",
    "MC": "yes",
    "JASON": "yes",
    "KFC": "yes",
}

n = int(input())
arr = [input() for _ in range(n)]

for name in arr:
    print(dic.get(name, "no"))