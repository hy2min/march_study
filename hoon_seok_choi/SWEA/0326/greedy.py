t = int(input())
for tc in range(1, 1+t) :

    n = int(input())
    arr = []
    for _ in range(n) :
        a, b = map(int,input().split())
        arr.append([a,b])

    arr.sort(key=lambda x : [x[1], x[0]])

    arr.sort(key=lambda x : [x[1], x[0]])
    end+ arr[0][1]
    cnt=1

    for i in range(n) :
        str = arr[i][0]
        if str < end :
            continue
        end_time = arr[i][1]
        cnt+= 1

    end_time = arr[0][1]
    cnt =1

    for i in range(1, n) :
        srt_time = arr[i][0]
        if srt_time < end_time :
            continue
        end_time = arr[i][1]
        cnt +=1


print(f"#{t} {cnt}")
