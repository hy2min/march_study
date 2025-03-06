N = int(input())
arr = [0]*1001
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H

Max = max(arr)
Max_idx = arr.index(Max)

for i in range(1001):
    if arr[i] != 0:
        left = i
        break
for i in range(1000, -1, -1):
    if arr[i] != 0:
        right = i
        break

# Max = 최대값 높이, Max_idx = 최대값 위치, left = 왼쪽, right = 오른쪽

left_arr = arr[left:Max_idx]
right_arr = arr[Max_idx+1:right+1]

S = Max # 넓이 제일 높은 기둥만큼 가지고 시작

Max_left = 0
for i in range(len(left_arr)):
    Max_left = max(Max_left, left_arr[i])
    S += Max_left

Max_right = 0
for i in range(len(right_arr)-1, -1, -1):
    Max_right = max(Max_right, right_arr[i])
    S += Max_right

print(S)