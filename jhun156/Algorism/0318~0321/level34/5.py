n = int(input())
if n == 1:
    print(1)
else:
    st = 2

    while st * st < n:

        st += 1

    print(st-1)