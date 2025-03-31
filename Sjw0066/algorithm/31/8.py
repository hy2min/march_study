str1=input()
N=int(input())

for _ in range(N):
    temp=str(int(str1)*2)
    lst=list(temp)
    lst.reverse()
    str1=''.join(lst)

print(str1)


