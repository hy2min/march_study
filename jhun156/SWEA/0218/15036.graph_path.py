# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())  # V = 노드 수, E = 간선 수
    lst = [list(map(int,input().split())) for _ in range(E)]    # 간선 루트
    S,G = map(int,input().split())  # 출발지(start), 목적지(goal)
    visited = [0] * (V + 1)         # while문 안에서 방문한 노드인지 확인하기 위한 지표
    connect = [[] for _ in range(V+1)]  # 연결 리스트, 내가 방문한 노드와 연결되어 있는 노드들을 표시한 리스트, 인덱스로 접근함 그렇기때문에 V+1 개로 만듦
    for i in range(E):
        connect[lst[i][0]].append(lst[i][1])    # 연결 리스트에 노드와 연관된 값들을 집어넣음

    def dfs(s,g):
        stack = [s]
        visited[s] = 1

        while True:
            present = stack.pop()   # 재탐색할 필요없이 pop을 통해 한번 지나온 경로 다시 볼 필요 없음
            if present == g:        # 만약 stack에 목적지와 같은 값이 들어있다면 경로가 있으므로
                return 1            # return 1

            for next_node in connect[present]:  # return 1이 실행되지 않았다면 현재 노드와 연결된 노드들을 탐색
                if not visited[next_node]:      # 연결된 노드들이 방문된 적이 없다면
                    visited[next_node] = 1      # visited에 1로 표시하고 재방문할 일이 없게함
                    stack.append(next_node)     # 연결된 노드들을 통해 재탐색
            if not stack:
                return 0                          # 이 while문을 통해 stack의 인자가 없다는 것은 연결된 노드가 없다는 뜻이 됨.

    ans = dfs(S,G)

    print(f"#{tc} {ans}")