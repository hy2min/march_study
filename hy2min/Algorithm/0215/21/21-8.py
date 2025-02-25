y,x = 5, 5
n = int(input())
arr = [input() for _ in range(n)]

def abc(y, x, i):
    if i == n:
        return
    
    if arr[i] =='down':
        abc(y+1, x, i+1)
    if arr[i] =='up':
        abc(y-1, x, i+1)
    if arr[i] =='left':
        abc(y, x-1, i+1)
    if arr[i] =='right':
        abc(y, x+1, i+1)
    if arr[i] == 'click':
        print(f'{y},{x}')
        abc(y, x, i+1)

abc(y,x,0)