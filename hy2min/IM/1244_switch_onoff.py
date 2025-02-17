n = int(input())
switch = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, idx = map(int, input().split())
    idx -= 1
    if gender == 1:
        times = 1
        while True:
            if times * idx >= n:
                break
            if switch[idx*times] == 1:
                switch[idx*times] = 0
            else:
                switch[idx*times] = 1
            times += 1

    if gender == 2:
        gap = 1
        if switch[idx] == 1:
            switch[idx] = 0
        while True:
            if idx - times < 0 or idx + times >= n or switch[idx - times] != switch[idx + times]:
                break
