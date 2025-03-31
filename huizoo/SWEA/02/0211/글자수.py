t = int(input())
for tc in range(1, t+1) :
    st1 = input()
    st2 = input()
    dic = {chr(65+i) : 0 for i in range(26)}
    for i in range(len(st1)) :
        dic[st1[i]] = st2.count(st1[i])
    print(f'#{tc} {max(dic.values())}')