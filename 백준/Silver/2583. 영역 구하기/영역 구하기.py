from collections import deque

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이미 있는 구간 체크하기
for i in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for x in range(sx, ex):
        for y in range(sy, ey):
            graph[y][x] = 1

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1
    area = 1

    while queue:
        curx, cury = queue.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                area += 1

    return area

answer = []
# bfs 시행 후 나온 넓이를 배열에 저장
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            answer.append(bfs(i, j))

# 길이 먼저 출력
print(len(answer))

for item in sorted(answer):
    print(item, end=' ')