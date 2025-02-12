#재귀함수
# N = int(input())
# def abc(level):
#
#     if level==N:
#         print(level,end=" ")
#         return
#     print(level, end=" ")
#     abc(level+1)
#     print(level, end=" ")
#
# abc(1)
#

# def abc(level):
#
#     if level==2:
#         return
#     for i in range(2):
#         abc(level+1)
#
#
#
# abc(0)

'''
위의 경우 트리의 구조를 가지는 재귀 함수로
트리의 가지수는 호출하는 함수의 개수
트리의 깊이는 종료조건으로 설정한 값에 따라 달라진다.
'''


# def abc(level):
#
#     if level==2:
#         return
#
#     for i in range(2):
#         print('.')
#         abc(level+1)
#         print('.')
# abc(0)

#소스코드위치에 따라 실행 타이밍이 너무 달라져서 잘 이해해야됨 ㅇㅇ

# 누적합 구하기
# arr=[3,4,5,1,6,9]
#
# #재귀로 구하기
# def sum_index(index,sum1):
#     sum1 += arr[index]
#     print(sum1,end=" ")
#
#     if index==len(arr)-1:
#         return
#
#     sum_index(index+1,sum1)
# sum_index(0,0)
#
# def abc(level,Sum):
#     print(Sum,end=" ")
#     if level ==5 :
#         return
#
#     abc(level+1,Sum+arr[level+1])
#
# abc(0,arr[0])

# Sum=arr[0]
#
# def abc(level):
#     global Sum
#     print(Sum,end=" ")
#     if level ==5 :
#         return
#     Sum += arr[level+1]
#     abc(level+1)
#
#
# abc(0)

#sum 변수의 값을 재귀가 리턴되면서 출력
# arr=[3,4,5,1,6,9]
#
# Sum=arr[0]
#
# def abc(level):
#     global Sum
#
#     if level ==5 :
#         print(Sum, end=" ")
#         return
#
#     Sum += arr[level+1]
#     abc(level+1)
#     Sum -= arr[level+1]
#     print(Sum, end=" ")
#
# abc(0)

# 점프
# 3 1 1 2
#
# arr=[2,0,1,1,3,5,1]
#
# def jump(st):
#     if st>len(arr)-1:
#         return
#
#     jump(st+arr[st])
#     print(arr[st],end=" ")
#
# jump(0)

# 3개의 카드 묶음이 있다.
# 각 묶음에는 3 또는 7 또는 1또는 2라는 값이 적혀있는 카드가 여러개 섞여있다.
#
# card=[3,7,1,2]
#
# Sum=0
# def draw_cards(level):
#     global Sum
#     if level == 3:
#         print(Sum,end=" ")
#         return
#
#
#     for i in range(4):
#         Sum+=card[i]
#         draw_cards(level+1)
#         Sum -= card[i]
#
# draw_cards(0,0)
#
# arr=[3,4,7,1,6]
#
# n=int(input())
# cnt=0
# def sum_cards(level,Sum):
#     global cnt
#
#     if Sum>10: # 백트래킹 back tracking 가지치기
#         return
#
#     if level==n: # 바닥조건
#         if Sum==10:
#             cnt+=1
#         return
#
#     for i in range(5):
#         sum_cards(level+1,Sum+arr[i])
#
#
#
# sum_cards(0,0)
# print(cnt)


# arr=['a','b','c']
# path=[" "]*2
#
# def abc(level):
#
#     if level==2:
#         print(*path)
#         return
#
#     for i in range(3):
#         path[level]=arr[i]
#         abc(level+1)
#
#
# abc(0)

# 중복 순열

# N=int(input())
# path=[0]*6
# def dice(level):
#     if level==N:
#         print(*path)
#         return
#
#     for i in range(6):
#
#         path[level] = i+1
#         dice(level+1)
#
# dice(0)

# 중복없이 뽑는 순열
# used를 통해 체크해준다.

# n=3
# card="ABCD"
# path=[""]*n
# used=[0]*len(card)
#
# def abc(level):
#     if level ==n:
#         print(*path)
#         return
#
#     for i in range(4):
#         if used[i] == 1 :
#             continue
#         path[level]=card[i]
#         used[i]=1
#         abc(level+1)
#         used[i]=0
#
#
# abc(0)

# 중복없는 조합
# card="ABCD"
# path=[""]*3
#
# def abc(level,st):
#     if level==3:
#         print(*path)
#         return
#     for i in range(st,4):
#         path[level]=card[i]
#         abc(level+1,i+1)
#         path[level]=0
# abc(0,0)

# 중복 있는 조합
# card="ABCD"
# path=[""]*3
#
# def abc(level,st):
#     if level==3:
#         print(*path)
#         return
#     for i in range(st,4):
#         path[level]=card[i]
#         abc(level+1,i) #### 여기만 바꿔주면 중복 여부 나옴
#         path[level]=0
# abc(0,0)

# B가 나오지 않는 경우 1.아예 진입을 안한다.
# dice=['A','B','C','D']
# N=3
# path=[0]*N
#
# def all_permutation(level):
#
#     if level==N:
#         print(*path)
#         return
#
#     for i in range(4):
#         if i != 1:
#             path[level] = dice[i]
#             all_permutation(level+1)
#             path[level] = 0
#
# all_permutation(0)

# 2. 들어갔다가 리턴으로 나온다.
# dice=['A','B','C','D']
# N=3
# path=[0]*N
#
# def all_permutation(level):
#
#     if level>0 and path[level-1] =='B':
#         return
#
#     if level==N:
#         print(*path)
#         return
#
#     for i in range(4):
#         if i != 1:
#             path[level] = dice[i]
#             all_permutation(level+1)
#             path[level] = 0
#
# all_permutation(0)


# 같은거 두개 연속 안나오게 하기
# dice=['A','B','C','D']
# N=3
# path=[0]*N
#
# def all_permutation(level):
#
#      if level>1 and path[level-1] == path[level-2]:
#          return
#
#      if level==N:
#         print(*path)
#         return
#
#      for i in range(4):
#         # if level>0 and path[level-1] == dice[i]: #진입 전 막기
#         #     continue
#         path[level] = dice[i]
#         all_permutation(level+1)
#         path[level] = 0
#
# all_permutation(0)

# 첫번째에서 c가 나오면 안됨

# dice=['A','B','C','D']
# N=3
# path=[0]*N
#
# def all_permutation(level):
#
#      if level==1 and path[0] == 'C':
#          return
#
#      if level==N:
#         print(*path)
#         return
#
#      for i in range(4):
#         if level==0 and i==2:
#             continue
#         path[level] = dice[i]
#         all_permutation(level+1)
#         path[level] = 0
#
# all_permutation(0)