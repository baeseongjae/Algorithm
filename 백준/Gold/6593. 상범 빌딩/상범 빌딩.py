from collections import deque
    
def BFS(x, y, z):
    queue = deque([(x, y, z)])
    visited[z][x][y] = 0
    while queue:
        curX, curY, curZ = queue.popleft()
        if graph[curZ][curX][curY] == 'E':
            print('Escaped in {0} minute(s).'.format(visited[curZ][curX][curY]))
            return
        for dx, dy, dz in d:
            nx = curX + dx
            ny = curY + dy
            nz = curZ + dz
            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and visited[nz][nx][ny] == -1:
                if graph[nz][nx][ny] == '.' or graph[nz][nx][ny] == 'E':
                    queue.append((nx, ny, nz))
                    visited[nz][nx][ny] = visited[curZ][curX][curY] + 1
    
    print('Trapped!')

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = []
    visited = [[[-1 for k in range(C)] for j in range(R)] for i in range(L)]
    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for _ in range(L):
        layer = [list(input()) for _ in range(R)]
        graph.append(layer)
        input()

    for k in range(L):
        for i in range(R):
            for j in range(C):
                if graph[k][i][j] == 'S':
                    BFS(i, j, k)
