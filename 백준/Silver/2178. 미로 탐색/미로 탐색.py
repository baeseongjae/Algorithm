import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] * (M) for _ in range(N)]
visited = [False] * (N)

for i in range(N):
    graph[i] = list(input().rstrip())
    graph[i] = list(map(int, graph[i]))

K = (1, 1)

def BFS(graph, startX, startY):
    queue = deque()
    queue.append((startX, startY))
    
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while queue:
        #현재 위치 꺼냄
        curX, curY = queue.popleft()

        #동서남북 방향으로 한번씩 이동하여 1인값 찾기
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            # 1인값을 찾았다면 이전 값의 +1하여 거리값 계산
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[curX][curY] + 1


BFS(graph, 0, 0)
print(graph[N-1][M-1])