T=int(input())
for test_case in range(1,T+1):
  N=int(input())
  boxes=list(map(int,input().split()))
  
  
  result=[0]*N

  for i in range(N):
    cnt=0
    for j in range(i+1,N):
      if boxes[i] > boxes[j]:
        cnt+=1
        result[i] = cnt
        
  print(result)
  result_max= max(result)
  
  print(f'#{test_case} {result_max}')