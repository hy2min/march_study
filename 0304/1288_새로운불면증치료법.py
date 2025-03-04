t = int(input())
for tc in range(1, t+1):
    n = int(input())
    st = set()


    i = 0
    while len(st) < 10:
        i += 1
        c_num = i * n
        st.update(str(c_num))
    
    print(f'#{tc} {c_num}')