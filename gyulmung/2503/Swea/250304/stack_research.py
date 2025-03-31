st = []
arr = input()
cnt = 0
ret = 1
while True:
    if cnt >= len(arr) and st:
        ret = 0
        break
    elif cnt >= len(arr):
        break

    if arr[cnt] == "(":
        st.append(arr[cnt])

    if arr[cnt] == ')':
        if st.pop() != '(':
            ret = 0
            break

    cnt += 1

print(ret)
