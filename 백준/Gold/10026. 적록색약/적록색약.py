from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque([])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cntA, cntB = 0, 0

def bfs(x, y):
    queue.append((x, y))

    while queue:
        curX, curY = queue.popleft()
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == graph[curX][curY]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

# 적록색약이 아닌 사람이 본 구역수
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cntA += 1

# 적록색약인 사람이 본 구역수
visited = [[0 for _ in range(N)] for _ in range(N)]
# G를 'R'로 변환
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cntB += 1

print(cntA, cntB)