t = int(input())
for tc in range(1, t+1):
    st = [list(input()) for _ in range(5)]
    max_len = len(max(st, key=len))
    for i in range(5):
        st[i].extend(['']*(max_len-len(st[i])))
    st2 = list(zip(*st))
    print(f'#{tc}', ''.join(''.join(row) for row in st2))