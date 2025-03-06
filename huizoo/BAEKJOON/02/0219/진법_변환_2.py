N, B = map(int, input().split())
st = ''
if B > 10:
    while N >= B:
        a = N % B
        if a < 10:
            st = str(a) + st
        elif a >= 10:
            st = chr(a+55) + st
        N //= B
    if N >= 10:
        st = chr(N+55) + st
    else:
        st = str(N) + st
elif B == 10:
    st = N
else:
    while N >= B:
        a = N % B
        st = str(a) + st
        N //= B
    st = str(N) + st
print(st)