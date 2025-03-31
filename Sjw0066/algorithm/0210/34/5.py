N=int(input())

ed=N
st=0

while st<=ed:
    if st**2<N:
        st+=1
    if ed**2>N:
        ed-=1

ans=ed
print(ans)
