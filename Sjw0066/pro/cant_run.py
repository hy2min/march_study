def solution(priorities, location):
    answer = 0

    lst = list(zip(list(range(len(priorities))), priorities))
    lst2 = []

    i = 0
    Max = -21e8
    Max_idx = 0
    while lst:
        Max = -21e8
        Max_idx = 0
        cnt=1
        while 1:
            if cnt==len(lst):
                break

            if Max < lst[i][1]:
                Max = lst[i][1]
                Max_idx = i
            i += 1
            cnt += 1

            if i == len(lst) and cnt<len(lst):
                i=0


        temp=lst.pop(Max_idx)
        lst2.append(temp)
        if temp[0]==len(priorities)-1:
            i=0
        elif len(lst)==Max_idx:
            i=Max_idx-1
        else:
            i=Max_idx


    for i in range(len(lst2)):
        if lst2[i][0] == location:
            answer = i+1
            break

    return answer

a=[1, 2, 9, 1, 1, 1]
b=0
print(solution(a,b))