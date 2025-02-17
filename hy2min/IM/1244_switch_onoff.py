t = int(input())
switch = list(map(int, input().split()))
students = int(input())
for i in range(students):
    gender, n = map(int, input().split())
    if gender == 1:
        for i in range(n-1, t, n):
            switch[i] = 1 - switch[i]


    elif gender == 2:
        idx = n- 1
        left, right = idx, idx

        while left > 0 and right < t-1 and switch[left-1] == switch[right+1]:
           left -= 1
           right += 1


        for i in range(left, right + 1):
            switch[i] = 1- switch[i]

for i in range(0,t,20):
    print(*switch[i:i+20])