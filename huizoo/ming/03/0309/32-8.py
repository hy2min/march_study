n = int(input())
arr = []
for _ in range(n):
    st = input()
    if st.istitle():
        arr.append(st)
        continue
    if st.isupper():
        arr.append(st)
        continue
    if st.islower():
        st = st.title()
    else:
        st = st.upper()
    arr.append(st)
for row in sorted(arr):
    print(row)