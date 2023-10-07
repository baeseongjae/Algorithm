# 섬의개수를 출력
# 1은 Land, 0은 바다
# BFS를 통해 구역수를 세는 문제 (같은 구역이 되려면 가로 혹은 세로 혹은 대각선 으로 인접해야함)
from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        curX, curY = queue.popleft()

        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            # 인덱스범위안에 있고 땅이고 방문하지 않았으면 방문
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

while True:
    try:
        data = input()
        if data == '0 0' or not data:
            break
        w, h = map(int, data.split())
        graph = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(h):
            graph[i] = list(map(int, input().split()))

        cnt = 0
        visited = [[0 for _ in range(w)] for _ in range(h)]
        # 구역 개수 구하기        
        for i in range(h):
            for j in range(w):    
                # 땅이고 방문하지 않은 노드면 방문.
                if graph[i][j] == 1 and not visited[i][j]:
                    BFS(i, j)
                    # 한번의 BFS끝날때마다 구역수 1증가
                    cnt += 1
        print(cnt)

    except:
        break