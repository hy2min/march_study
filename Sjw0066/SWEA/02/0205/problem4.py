

T=10

for test_case in range(1,T+1):
    N=int(input())
    bulding= list(map(int,input().split()))
    
    answer = 0 
    for i in range(2,N-2):
        max_left=-1e21
        max_right=-1e21
        max_total=0

        for j in range(1,3):
            if max_left<bulding[i-j]:
                max_left = bulding[i-j]
            
            if max_right < bulding[i+j]:
                max_right = bulding[i+j]
        
        if max_right<max_left:
            max_total=max_left
        else:
            max_total=max_right
        
        if bulding[i] - max_total > 0 :
            answer += bulding[i] - max_total
        
    print(f'#{test_case} {answer}')