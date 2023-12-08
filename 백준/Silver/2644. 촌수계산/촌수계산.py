from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
queue = deque([])

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def BFS(a, b):
    queue.append([a, 0])
    visited[a] = 1

    while queue:
        cur, depth = queue.popleft()

        if cur == b:
            return depth

        for next in graph[cur]:
            if not visited[next]:
                queue.append([next, depth+1])
                visited[next] = 1

    return -1

print(BFS(a, b))