T = int(input())

for tc in range(1, T + 1):
    K,N,M = map(int, input().split())
    bus_stops = list(map(int, input().split()))


    last_charge=0
    loc=0
    cnt=0


    while last_charge+K<N:
        flag = 0
        for i in range(last_charge+K,last_charge,-1):
            if i in bus_stops :
                cnt += 1
                last_charge = i
                flag=1
                break

        if flag==0:
           cnt=0
           break





    print(f'#{tc} {cnt}')