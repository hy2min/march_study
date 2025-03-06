# import copy
# T=int(input())
#
# def queen(y,x):
#     global arr
#
#     if arr[y][x] == 1:
#         return False
#
#     for i in range(9):
#         for j in range(1,N):
#             dy=direct_y[i]*j+y
#             dx=direct_x[i]*j+x
#             if dy>N-1 or dy<0 or dx>N-1 or dx<0:break
#             if arr[dy][dx] == 1: continue
#             arr[dy][dx] = 1
#
#     return True
#
# def n_queen(level):
#     global cnt,arr
#
#     if level==N:
#         cnt+=1
#         return
#
#     temp = copy.deepcopy(arr)
#
#     for i in range(N):
#         if arr[level][i] == 1: continue
#         if used[i] == 1: continue
#         if queen(level,i) :
#             used[i] = 1
#             n_queen(level+1)
#             used[i] = 0
#             arr=copy.deepcopy(temp)
#         else:
#             continue
#
#
#
#
# for tc in range(1,T+1):
#     N=int(input())
#     arr=[[0]*N for _ in range(N)]
#     direct_y=[-1,-1,-1,0,0,0,1,1,1]
#     direct_x=[-1,0,1,-1,1,0,-1,0,1]
#     cnt=0
#     used=[0]*N
#     n_queen(0)
#
#     print(f'#{tc} {cnt}')

import copy
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N=int(input())
    Map=[[0]*N for _ in range(N)]
    directx=[-1,0,1,-1,1,-1,0,1,0]
    directy=[-1,-1,-1,0,0,1,1,1,0]
    Count=0

    def change(y,x):
        for i in range(9):
            for j in range(1, N):
                dy = y + directy[i] * j
                dx = x + directx[i] * j
                if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1: break
                if Map[dy][dx] == 1: continue
                Map[dy][dx] = 1

    def DFS(level):
        global Map,Qeen,Count

        if level == N:
            Count += 1
            return
        for i in range(N):
            for j in range(N):
                if Map[i][j]==0:
                    Map[i][j] = 1
                    temp = copy.deepcopy(Map)
                    change(i,j)
                    DFS(level+1)
                    Map=copy.deepcopy(temp)
        # for i in range(N):
        #     # 현재 행에서 i번째 열에 퀸을 놓을 수 있다면
        #     if Map[level][i] == 0:
        #         # 퀸을 놓기 전에 상태를 백업
        #         temp = copy.deepcopy(Map)
        #
        #         # 퀸을 놓고 해당 위치와 그 범위를 공격 영역으로 설정
        #         Map[level][i] = 1
        #         change(level, i)
        #
        #         # 다음 행으로 DFS를 진행
        #         DFS(level + 1)
        #
        #         # 상태를 복원 (백트래킹)
        #         Map = copy.deepcopy(temp)

    DFS(0)
    print(f'#{test_case} {Count}')
    # ///////////////////////////////////////////////////////////////////////////////////
