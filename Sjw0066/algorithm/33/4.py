N,K=map(int,input().split())
lst=[[] for _ in range(K+1)]
name=['']*(K+1)
for i in range(N):
    # a랑 b가 둘다 숫자면 그룹묶기
    # a랑 b가 글자가 하나 있으면 그놈을 등급으로 매기기
    a,b=input().split()


    if a.isdecimal() and b.isdecimal():
        lst[int(a)].append(int(b))
        lst[int(b)].append(int(a))
    else:
        if a.isalpha():
            name[int(b)] = a
        else:
            name[int(a)] = b




