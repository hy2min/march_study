t = int(input())
for tc in range(1, t+1):
    st1 = input()
    st2 = input()
    Max = 0
    for i in st1:
        cnt = st2.count(i)
        if Max < cnt:
            Max = cnt
    print(f'#{tc} {Max}')