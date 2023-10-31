from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1), 
     (-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
queue = deque()

def BFS():
    while queue:
        curX, curY = queue.popleft()

        for dx, dy in d:
            nx = curX + dx
            ny = curY + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[curX][curY] + 1
                    queue.append((nx, ny))

# 상어좌표 전부 큐에 삽입
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0

# 큐에 좌표 삽입했으니, BFS 시행
BFS()

# BFS 종료후 visited에 삽입된 안전거리의 최댓값 구하기
maxValue = 0
for row in visited:
    maxValue = max(maxValue, max(row))

print(maxValue)

# 상어가 있는 1인 좌표에서 부터 BFS시행 (최단거리를 잼)