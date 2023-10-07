from collections import deque

def BFS(curX, curY, cnt):
    queue = deque()
    queue.append(((curX, curY), cnt))
    visited[curX][curY] = 1
    
    while queue:
        (curX, curY), cnt = queue.popleft()

        if curX == desX and curY == desY:
            print(cnt)
            return
        
        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                queue.append(((nx, ny), cnt+1))
                visited[nx][ny] = 1

T = int(input())

for _ in range(T):
    I = int(input())
    curX, curY = map(int, input().split())
    desX, desY = map(int, input().split())
    
    visited = [[0 for _ in range(I)] for _ in range(I)]
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    cnt = 0

    BFS(curX, curY, cnt)


# 체스에서 나이트의 능력대로 이동하면서 목표지점까지의 최소 연산횟수를 구하는 문제
# BFS