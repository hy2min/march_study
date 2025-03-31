dino = {
    'Sour': 1000000005,
    'Dav': 1000000002,
    'Nica': 1000000003,
    'Timer': 1000000006,
    'Pico': 1000000015,
    'Topisl': 1000000022,
    'Whab': 1000000013,
    'Hap': 1000000009,
}

n = int(input())
for i in dino.keys():
    if dino[i] == n:
        print(i)
        break