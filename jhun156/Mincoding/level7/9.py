arr = [i for i in map(int,input().split())]
cnt = 1

for i in arr:
    if i >= 70:
        print(f"{cnt}번사람은{i}점PASS")
        cnt += 1
    elif i >= 50:
        print(f"{cnt}번사람은{i}점RETEST")
        cnt += 1
    else:
        print(f"{cnt}번사람은{i}점FAIL")
        cnt += 1
