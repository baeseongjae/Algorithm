import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
E = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

#연결된 모든 노드 수 구하면 됨.

def BFS(graph, start):
    queue = deque()
    queue.append(start)
    cnt = 0

    while queue:
        cur = queue.popleft()

        # 방문하지 않은 노드라면
        if not visited[cur]:
            # 방문!
            visited[cur] = True
            cnt += 1
            for node in graph[cur]:
                queue.append(node)

    answer = cnt - 1
    print(answer)

BFS(graph, 1)
