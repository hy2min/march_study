oil = input()

def parametric_search(str):
    st = 0
    ed = len(str) - 1
    ans = -1
    while True:
        mid = (st + ed) // 2
        if str[mid] == "#":
            st = mid + 1
            ans = mid
        elif str[mid] == "_":
            ed = mid -1
        if st > ed:
            break
    return ans

ret = parametric_search(oil)
ans = (ret+1)*10
print(f"{ans}%")