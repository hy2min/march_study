collect=['A','P','P','L','E','T']

lst1=list(map(str,input().split()))

answer=0
for i in lst1:
    answer += collect.count(i)

print(f'{answer}개 맞추었습니다')
