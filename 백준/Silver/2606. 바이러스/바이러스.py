import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
E = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

#연결된 모든 노드 수 구하면 됨.
def BFS(start):
    queue = deque([start])
    visited[start] = 1
    cnt = 0

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                cnt += 1
                visited[next] = 1
    return cnt

print(BFS(1))