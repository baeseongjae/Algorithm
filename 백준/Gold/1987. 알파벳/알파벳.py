R, C = map(int, input().split())
arr = [list(input()) for i in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)] 
checked = [0] * 27
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# 아스키코드 활용하여 알파벳 => 숫자로 바꾸기
for i in range(R):
    for j in range(C):
        arr[i][j] = ord(arr[i][j]) - 64

def DFS(x, y, cnt):
    global answer
    answer = max(cnt, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 있고, 방문안한 노드인지
        # arr[nx][ny]가 기존 알파벳들과 다른 알파벳인지
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            if not checked[arr[nx][ny]]:
                visited[nx][ny] = 1
                checked[arr[nx][ny]] = 1
                DFS(nx, ny, cnt+1)
                visited[nx][ny] = 0
                checked[arr[nx][ny]] = 0
            

visited[0][0] = 1
checked[arr[0][0]] = 1
DFS(0, 0, 1)

print(answer)