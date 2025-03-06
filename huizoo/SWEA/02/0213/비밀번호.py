def dfs():
    global st
    same = 0
    n = len(st)-1
    i = 0
    while i < n:
        if st[i] == st[i+1]:
            same = 1
            st.pop(i)
            st.pop(i)
            n -= 2
            i -= 1
        i += 1
    if same:
        dfs()
    else:
        print(f'#{tc} {"".join(st)}')

for tc in range(1, 11):
    inputs = list(input().split())
    st = list(inputs[1])
    dfs()
