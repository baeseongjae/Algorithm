from collections import deque
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input())
graph = [0] * N
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인풋값으로 그리드 판 채우기
for i in range(N):
    graph[i] = list(input())

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        curX, curY = queue.popleft()
        # 다음 next좌표를 상하좌우로 찾는 로직
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            # 인덱스 범위안에 있고 방문하지 않은 좌표이면 탐색
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 같은 색상이면 
                if graph[curX][curY] == graph[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

# BFS 활용하여 적록색약이 아닌 사람이 보는 section수 출력 로직
cnt1 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt1 += 1

# BFS 활용하여 적록색약인 사람이 보는 section수 출력 로직   
cnt2 = 0
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt2 += 1

print(cnt1, cnt2)