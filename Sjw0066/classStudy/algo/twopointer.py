# 구간합을 구할때 구간의 크기가 정해져 있지않은경우
# two pointer
# n,m 입력
# n개의 자연수중 연속된 숫자의 합이 m이 되는 경우 몇가지인가?
# right left를 만들고 m보다 작으면 right +=1 , 크면 left +=1

n,m=11,5

lst=[1,2,3,4,2,5,3,1,1,2,5]
Sum=0
cnt=0
right=0

for left in range(n):

    while(Sum<m and right<=n):
        Sum+=lst[right]
        right+=1

    if Sum==m:
        cnt+=1

    Sum -= lst[left]

print(cnt)
