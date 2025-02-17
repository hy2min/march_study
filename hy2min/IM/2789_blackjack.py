N, M = map(int, input().split())
cards = list(map(int, input().split()))
used = [0] * N
Max_n = 0
def abc(level,Sum):
    global Max_n
    if level == 3:
        if Sum <= M:
            if Max_n < Sum:
                Max_n = Sum
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            abc(level+1, Sum + cards[i])
            used[i] = 0

abc(0,0)
print(Max_n)