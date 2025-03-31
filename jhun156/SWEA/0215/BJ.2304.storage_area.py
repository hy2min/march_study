import sys
sys.stdin = open("input.txt","r")

N = int(input())
lst = [[0] * N for _ in range(2)]   # lst[0],lst[1]을 각각 인덱스와 높이로 활용
arr = [list(map(int,input().split())) for _ in range(N)]    # 문제 입력값
for i in range(N):
    lst[0][i] = arr[i][0]
    lst[1][i] = arr[i][1]
Max = max(lst[1])           # 가장 높은 높이
Max_index = 0               # 값을 계산하기 위한 기준점 찾기
for i in range(N):
    if lst[1][i] == Max:
        Max_index = lst[0][i]   # 가장 오른쪽의 맥스값과 같은 인덱스
area = 0                 # 가장 높은 값의 인덱스 기준으로 양옆까지만 계산할 것이기 때문에 넓이 = Max 부터 시작함
st = min(lst[0])            # column 에서 시작점 인덱스
ed = max(lst[0])            # column 에서 끝점 인덱스
column = [0] * (ed+1)       # column 생성 1000개 생성할 필요없이 ed를 활용해 크기를 줄임
for i in range(N):          # Runtime 에러를 일으키지 않기 위함
    column[lst[0][i]] = lst[1][i]   # column 에 높이값들 입력

ph = column[st]             # 현재 기준점 높이
while st < Max_index:       # Max 인덱스가 될때까지 반복
    if column[st] <= ph:    # 현재 높이보다 높은게 나오면 변경해주며 넓이를 순차적으로 계산
        area += ph          # 좌측 시작점부터 Max_index까지
        st += 1
    else:
        ph = column[st]
        area += ph
        st += 1

ph = column[ed]
area += ph
ed -= 1

while ed >= Max_index:
    if column[ed] <= ph:
        area += ph
        ed -= 1
    else:
        ph = column[ed]
        area += ph
        ed -= 1
print(area)