from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxNum = 0
maxValue = 0

def BFS(x, y, k):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        curX, curY = queue.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > k and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

# 입력받은 2차원 배열에서 최댓값 찾는다
for row in graph:
    for item in row:
        maxNum = max(item, maxNum)

# 조건에 맞는 좌표를 시작점으로 BFS 강행
for k in range(maxNum + 1):
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                BFS(i, j, k)
                cnt += 1
    maxValue = max(cnt, maxValue)
    
print(maxValue)