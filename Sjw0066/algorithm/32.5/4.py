N=int(input())
down=[]
up=[]
for i in range(N):
    a,b = input().split()
    if b=='DOWN':
        down.append(int(a))
    else:
        up.append(int(a))

st=0
ed=50
for i in down:
    if i<ed:
        ed=i
for i in up:
    if i>st:
        st=i

if st>ed:
    print('ERROR')
elif ed-st==2:
    print(st+1)
else:
    print(f'{st+1} ~ {ed-1}')