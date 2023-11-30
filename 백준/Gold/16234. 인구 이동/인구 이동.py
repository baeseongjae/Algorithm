from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
day = 0

# 여기서 BFS함수는 하루동안 연합인 국가를 정의하는 역할.
def BFS(x, y):
    queue = deque([(x, y)])
    union.append((x, y))
    visited[x][y] = 1

    while queue:
        curX, curY = queue.popleft()

        for dx, dy in d:
            nx = curX + dx
            ny = curY + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:  
                gap = abs(A[nx][ny] - A[curX][curY])
                # 조건 통과하면 연합 형성. 그러고 방문.
                if L <= gap <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    
    if len(union) > 1:
        return True
    else:
        return False

# 하루 동안 인구 이동 로직.
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    exist = 0

    # 연합국이 여러개 일 수 있으므로 for문 돌려서 BFS시행 (방문한 지역 제외)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = []
                # BFS 시행 후 연합국가 있으면
                if BFS(i, j):
                    exist = 1
                    people = sum(A[x][y] for x, y in union)
                    for x, y in union:
                        A[x][y] = people // len(union) 
    
    if not exist:
        print(day)
        break      
    day += 1