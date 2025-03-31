# 시작점을 모를때 수행
# 모든 시작점에서 다른 모든 정점까지 최소비용 계산
# 속도가 느림 n3 임 ㅇㅇ
inf=21e8
arr=[
    [0,5,inf,8],
    [7,0,9,inf],
    [2,inf,0,4],
    [inf,inf,3,0],
]

for ky in range(4):
    for si in range(4):
        for do in range(4):
            if arr[si][do] > arr[si][ky]+arr[ky][do]:
                arr[si][do] = arr[si][ky]+arr[ky][do]

# 하면 값 갱신 끝남 ㅇㅇ
