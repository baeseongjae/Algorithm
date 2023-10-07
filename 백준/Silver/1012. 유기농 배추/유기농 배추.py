from collections import deque

def BFS(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        cr, cc = queue.popleft()        
        
        for i in range(4):
            nr = cr + dx[i]
            nc = cc + dy[i]

            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1

# 테스트 케이스 입력값 부터 받아서 시작.
T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 입력값(배추좌표)받아 배추밭 채우기
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
  
    # 구역 수 구하기
    cnt = 0
    for c in range(M):
        for r in range(N):
            #배추 있고 방문하지 않은 배추좌표만 탐색
            if graph[r][c] and not visited[r][c]:
                BFS(r, c)
                cnt += 1
    print(cnt)