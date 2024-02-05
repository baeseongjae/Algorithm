from collections import deque

T = int(input())
d = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]


def bfs(sx, sy):
    queue = deque()
    queue.append([(sx, sy), 0])
    visited[sx][sy] = 1

    while queue:
        (curX, curY), cnt = queue.popleft()

        if curX == endX and curY == endY:
            return cnt

        for (dx, dy) in d:
            nx = curX + dx
            ny = curY + dy

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                queue.append([(nx, ny), cnt + 1])
                visited[nx][ny] = 1

for i in range(T):
    l = int(input())
    visited = [[0 for _ in range(l)] for _ in range(l)]

    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())

    print(bfs(startX, startY))