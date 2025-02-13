T = int(input())
for idx in range(T):
    s = list(input())
    i = 0
    while True:
        if i == len(s)- 1:
            break

        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1

    print(f'#{idx+1} {len(s)}')
