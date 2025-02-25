#
# '''
# parametric search
# bettery="###_______"
#
# '''
# bettery = "__________"
#
#
# def parametric_search(st, ed, target):
#     Max = -1
#     while 1:
#         mid = (st + ed) // 2
#
#         if bettery[mid] == target:
#             Max = mid
#             st = mid + 1
#
#         if bettery[mid] != target:
#             ed = mid - 1
#
#         if st > ed:
#             break
#     return Max + 1
#
#
# ret = parametric_search(0, len(bettery), '#')
# print(ret * 10)

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

# y 파라메트릭 서치 돌리고 x 파라메트릭 서치 돌리기
def binary_search(start,end):
    Max=-1
    while 1:
        mid=(start+end)//2
        if curser[mid][0]=='_':
            end=mid-1
        elif curser[mid][0]=='#':
            Max=mid
            start=mid+1
        if start>end:
            break
    return Max+1

def binary_search2(start,end,y):
    Max=-1
    while 1:
        mid=(start+end)//2
        if curser[y][mid]=='_':
            end=mid-1
        elif curser[y][mid]=='#':
            Max=mid
            start=mid+1
        if start>end:
            break
    return Max+1

yaxis=binary_search(0,5)
yaxis-=1
xaxis=binary_search2(0,9,yaxis)
print(yaxis,xaxis)

