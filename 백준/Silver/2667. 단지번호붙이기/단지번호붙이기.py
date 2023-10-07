from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
section = 0
answer = []

def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    home = 0

    while queue:
        curX, curY = queue.popleft()
        home += 1
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
        
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

    return home


for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            home = BFS(i, j)
            answer.append(home)
            section += 1

print(section)

answer.sort()
for item in answer:
    print(item)