n = int(input())
for _ in range(n):
    cnt = 0
    s = input()
    for i in s:
        cnt = cnt * 26 + (ord(i) - ord('A'))
    cnt += 1
    print(cnt)