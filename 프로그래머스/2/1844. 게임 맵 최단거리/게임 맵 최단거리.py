from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N = len(maps)       # 행이 수
    M = len(maps[0])    # 열의 수
    visited = [[0 for i in range(M)] for _ in range(N)]
    
    def BFS(x, y):
        queue = deque([(x, y)])
        visited[0][0] = 1
        
        while queue:
            curX, curY = queue.popleft()
                
            for i in range(4):
                nx = curX + dx[i]
                ny = curY + dy[i]
                    
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[curX][curY] + 1
        
    
    BFS(0, 0)
    answer = visited[N-1][M-1]
    
    if answer == 0:
        answer = -1
    
    return answer