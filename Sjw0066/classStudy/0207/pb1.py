# 모든 좌표로 부터 상하좌우 값 확인한다.

# 규칙 1.
# 기준 좌표로 부터 상하좌우의 범위가 배열범위를 넘어가면 무조건 0점처리

# 규칙 2.
# 1. 상하좌우의 합에서 기준좌표의 값을 뺀다.
# 1-1 상하좌우의 합에서 기준좌표의 값을 뺀 값이 음수라면 0점
# 1-2 상하좌우의 합에서 기준좌표의 값을 뺀 값이 짝수면 점수 2배하기

# 입력예제
"""
  테스트케이스의 개수를 입력 받는다.
  배열의 크기 N을 입력받은후
  N*N 사이즈 배열에 들어갈 값을 입력 받는다.
"""

# 출력결과
# 상하좌우의 합중 Max값 출력하기
T=int(input())

for tc in range(1,T+1):
        N=int(input())
        arr=[list(map(int,input().split())) for _ in range(N)]
        direct_y=[1,-1,0,0]
        direct_x=[0,0,1,-1]

        def score(y,x):
                sum1=0
                for i in range(4):
                        ny=y+direct_y[i]
                        nx=x+direct_x[i]
                        if ny>N-1 or ny<0 or nx>N-1 or nx<0:
                                return 0

                        sum1 += arr[ny][nx]
                result=sum1 - arr[y][x]

                if  result<0 :
                        return 0
                if result % 2 ==0 :
                        return result*2

                return result

        max_sum=-21e8
        for i in range(N):
                for j in range(N):
                        sum1=score(i,j)
                        if sum1>max_sum:
                                max_sum=sum1

        print(max_sum)


