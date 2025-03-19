def inorder(x, num):
    if x > N: return num
    num = inorder(2*x, num)
    arr[x] = num
    num += 1
    num = inorder(2*x+1, num)
    return num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]*(N+1)
    inorder(1, 1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')
