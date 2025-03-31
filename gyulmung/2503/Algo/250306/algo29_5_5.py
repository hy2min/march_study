# 블럭 채우기
arr = [list(map(int, input().split())) for _ in range(4)]

st = []
ed = []
# 시작 지점 찾기(왼쪽위의 좌표)
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            st.append((i, j))
            break
    if st:
        break

# 끝 지점 찾기(오른쪽 아래의 좌표)
for i in range(3, -1, -1):
    for j in range(4, -1, -1):
        if arr[i][j] ==1:
            ed.append((i, j))
            break
    if ed:
        break

print(f'({st[0][0]},{st[0][1]})')
print(*ed)