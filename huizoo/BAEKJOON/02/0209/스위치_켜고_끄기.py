N = int(input())
switches = list(map(int, input().split()))
student = int(input())
for _ in range(student) : 
    gender, switch = map(int, input().split())
    if gender == 1 : 
        temp = 1
        while switch*temp - 1 < N : 
            switches[switch*temp-1] = (switches[switch*temp-1] + 1) % 2
            temp += 1
    else : 
        temp = 1
        switches[switch-1] = (switches[switch-1] + 1) % 2
        while 1 :
            if (
                0 <= switch-1-temp < N and 0 <= switch-1+temp < N and
                switches[switch-1-temp] == switches[switch-1+temp]
            ) : 
                switches[switch-1-temp] = (switches[switch-1-temp] + 1) % 2
                switches[switch-1+temp] = (switches[switch-1+temp] + 1) % 2
            else : 
                break
            temp += 1

for i in range(0, len(switches), 20) : 
    print(*switches[i:i+20])