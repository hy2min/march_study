def same(st):
    length = len(st)
    same_idx = -1
    for i in range(length-1):
        if st[i] == st[i+1]:
            same_idx = i
    if same_idx == -1:
        return length
    else:
        for _ in range(2):
            st.pop(same_idx)
        length = same(st)
    return length

t = int(input())
for tc in range(1, t+1):
    st = list(input())
    ans = same(st)
    print(f'#{tc} {ans}')