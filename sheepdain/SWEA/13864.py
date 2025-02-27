def abc(i,j):
    if i==j:
        return i
    elif j==i+1:
        return ret(i,j)
    else:
        return ret(abc(i,(i+j)//2),abc((i+j)//2+1,j))
 
def ret(a,b):
    a_n,b_n=arr[a],arr[b]
    if a_n-b_n==-2 or a_n-b_n==1 or a_n==b_n:
        return a
    elif a_n-b_n==2 or b_n-a_n==1:
        return b
 
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.insert(0,0)
    ans=abc(1,n)
 
    print(f'#{test_case}',ans)