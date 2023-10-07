from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
relyList = [0] * (N+1)
answer = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)

def BFS(node, graph):
    visited = [False] * (N+1)
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        cur = queue.popleft()
        for v in graph[cur]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                relyList[v] += 1

for i in range(1, N+1):
    BFS(i, arr)

maxValue = max(relyList)

for index, value in enumerate(relyList):
    if value == maxValue:
        answer.append(index)

answer.sort()
print(*answer)
