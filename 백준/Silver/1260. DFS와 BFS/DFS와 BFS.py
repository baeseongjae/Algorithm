import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

for i in range(1, n + 1):
    arr[i].sort()

def DFS(node):
    print(node, end = ' ')
    visited[node] = True

    for v in arr[node]:
        if visited[v] == False:
            DFS(v)

DFS(v)
print()



visited = [False] * (n + 1)   # 리스트 초기화

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while len(queue) > 0:
        cur = queue.popleft()
        print(cur, end = ' ')

        for v in arr[cur]:
            if visited[v] == False:
                visited[v] = True
                queue.append(v)

BFS(v)