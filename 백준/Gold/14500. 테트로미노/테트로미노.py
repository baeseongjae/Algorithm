import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
answer = 0
def isValid(r, c):
    if 0 <= r < N and 0 <= c < M:
        return True
    return False

def DFS(x, y, depth, total):
    global answer

    if depth == 4:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not isValid(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            
            if depth == 2:
                visited[nx][ny] = 1
                # total += arr[nx][ny]
                DFS(x, y, depth+1, total+arr[nx][ny])
                visited[nx][ny] = 0

            visited[nx][ny] = 1
            # total += arr[nx][ny]
            DFS(nx, ny, depth+1, total+arr[nx][ny])
            visited[nx][ny] = 0


# for 문 돌려서 DFS 시행.
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(answer)
