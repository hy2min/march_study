#
# T = int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     stone=list(map(int,input().split()))
#
#     for _ in range(M):
#         a,b = map(int,input().split())
#
#         for i in range(1,b+1):
#                index=a+i-1
#                rev_index=a-i-1
#
#
#                if index > N-1 or rev_index<0:
#                    break
#
#                if stone[index] == stone[rev_index]:
#                     stone[index] = 1-stone[index]
#                     stone[rev_index] = 1-stone[rev_index]
#
#
#     print(f'#{tc}',end=" ")
#     for i in range(N):
#         print(stone[i],end=" ")
#     print()


lst=[
['_','_','_','_','B','_','_',],
['_','_','_','_','_','_','_',],
['_','A','A','_','_','_','_',],
['_','_','_','_','_','_','_',],
['_','_','A','_','_','_','_',],
['_','#','#','_','B','_','_',],
['_','_','_','_','#','_','_',]]

# 7*7 배열
# A는 5칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# B는 3칸 떨어진 곳 까지 상하좌우 물풍선이 터져서 퍼진다.
# '#'은 벽이다
# 벽 그리고 A,B 뒤로는 물풍선이 터지지 않는다.

# 물을 피할곳은 지도상 몇군데인가? - 16 -

#
# direct_x=[0,0,-1,1]
# direct_y=[1,-1,0,0]
# def water_bomb(bomb,y,x):
#     global lst
#     for i in range(4):
#         for j in range(1,bomb+1):
#             ny=y+direct_y[i]*j
#             nx=x+direct_x[i]*j
#             if ny>6 or ny<0 or nx>6 or nx<0:
#                 continue
#             if lst[ny][nx] != "_" and lst[ny][nx] != 'O':
#                 break
#             if lst[ny][nx] == "_":
#                 lst[ny][nx] = "O"
#
#
# for i in range(7):
#     for j in range(7):
#         if lst[i][j] == 'A':
#             water_bomb(5,i,j)
#         elif lst[i][j] == 'B':
#             water_bomb(3,i,j)
# for i in lst:
#     print(i)
# cnt=0
# for i in range(7):
#     for j in range(7):
#         if lst[i][j] == '_':
#             cnt+=1
#
# print(cnt)
