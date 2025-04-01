# 정렬이 되어있는 data 필수
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
# def binary_search(st, ed, target):
#     while 1:
#         mid = (st+ed)//2
#         if mid == target : return 1
#         elif mid > target : ed = mid
#         elif mid < target : st = mid
#         if st > ed : return 0
#
#
# arr.sort()
# ans = binary_search(0, n-1, target)
#
# if ans:
#     print('웃기다')
# else:
#     print('가볍다')

# Parametric search - max라는  변수를 만들어 변수에 미드 값을 항상 저장한다.

# N = int(10)
# battery = input()
#
# def parametric_search(st, ed):
#     Max = 0
#     mid = (st+ed)//2
#     if battery[mid] == '#':
#         Max = mid
#         st = mid + 1
#     elif battery[mid] == '_':
#         ed = mid - 1
#     if st > ed:
#         breakpoint()

# remain_battery = parametric_search(0, N -1)
# # '###_______'

# 워드작업 중 정전으로 인하여 컴퓨터가 강제로 종료가 되었습니다.
# 다시 전기가 들어어 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을때 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그래밍을 완성해 주세요.
# 시간복잡도 (On^2)보다 빨라야 합니다.

# 6*10 size 리스트 (배열)

curser=[
    '##########',
    '##########',
    '###_______',
    '__________',
    '__________',
    '__________']

def find_curser(st, ed):
    where = 0
    mid = (st+ed)//2
    if find_curser[mid][0] == "#":
        where = mid
        st = mid + 1
    elif find_curser[mid][0] == '_':
        ed = mid - 1
    if st > ed: return where

def find_curser_row(st, ed, col):
    where = 0
    mid = (st+ed)//2
    if find_curser[col][mid] == "#":
        where = mid
        st = mid + 1
    elif find_curser[col][mid] == '_':
        ed = mid - 1
    if st > ed: return where

col = find_curser(0, 5)
Find = find_curser_row(0, 9, col)
print(col, Find)