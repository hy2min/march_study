#a 50
#b 40
#c 99
#d 5
#e 25
#f 6
#g 37

# 서바이벌 선수와 전투력이 있을때
# a~f를 두 팀으로 만들어서 서바이벌 게임을 하고자 한다.
# 두 팀의 전투력 차이가 가장 적게하여 두 팀을 구성한다고 했을때
# 두 팀의 최소 전투력 차이는 몇이 되는가?
# 모든 선수는 서바이벌에 참가하며 1인팀도 가능합니다.
# 조합을 구성

power=[50,40,99,5,25,6,37]
visited = [0]*7
Total = sum(power)
print(Total)
Min = 1e8
TeamA = []

def dfs(level):
    global Min, TeamA
    Min = min(Min, abs(sum(TeamA)*2 - Total))
    if level == 4:
        return

    for i in range(7):
        if visited[i] == 0:
            visited[i] = 1
            TeamA.append(power[i])
            dfs(level+1)
            visited[i] = 0
            TeamA.pop()

dfs(1)
print(Min)

# 하균이형 소스코드
def power_t(team1,team2):
    global Min_t
    if used.count(1) == 7:
        if abs(sum(team1) - sum(team2)) < Min_t:
            Min_t =abs(sum(team1)- sum(team2))
            print(team1,team2)
        return
    for i in range(7):
        if used[i] == 0 and  sum(team1) <= sum(team2):
            used[i] = 1
            power_t(team1 + [power[i]],team2)
            used[i] = 0
        if used[i] == 0 and sum(team2) < sum(team1):
            used[i] = 1
            power_t(team1,team2 + [power[i]])
            used[i] = 0



power = [50,40,99,5,25,6,37]
used = [0]*7
Min_t = 1000
power_t([0],[0])
print(Min_t)

# 강사님 소스코드
power=[50,40,99,5,25,6,37]

total=sum(power)
Min=21e8
def dfs(level,start,Sum):
    global Min
    against=0
    against=total-Sum
    gap=abs(Sum-against)
    Min=min(gap,Min)

    if level==6:
        return
    for i in range(start,7):
        dfs(level+1,i+1,Sum+power[i])
dfs(0,0,0) # level start Sum
print(Min)