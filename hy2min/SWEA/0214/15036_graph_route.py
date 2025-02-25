
def find_route(route, S, G, V):
    start = [S]
    used = [0] * (V+1)

    while start:
        node = start.pop()

        if node == G:
            return 1
        
        if not used[node]:
            used[node] = 1
            start.extend(route[node])
        
    return 0


T = int(input())
for idx in range(T):
    V, E = map(int, input().split())
    route = [[] for _ in range(V+1)]

    for i in range(E):
        s, g = map(int,input().split())
        route[s].append(g)
    S, G = map(int, input().split())

    res = find_route(route, S, G, V)
    print(f'#{idx+1} {res}')