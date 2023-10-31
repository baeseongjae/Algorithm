import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
# N 행 , M 열
graph = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
possible = False
answer = []

# 입력값 받아서 맵 채우기
for i in range(N):
    graph[i] = list(map(int, input().rstrip()))

def BFS(x, y):
    global possible
    queue = deque([(x, y, 0, 1)])

    while queue:
        curX, curY, crush, cnt = queue.popleft()

        # 목표 좌표에 도달했다면 서치 종료
        if curX == N-1 and curY == M-1:
            possible = True
            answer.append(cnt)

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            # 인덱스 범위 체크 
            if 0 <= nx < N and 0 <= ny < M:
                # 방문안한 노드라면 
                if not visited[nx][ny][crush]:
                    visited[nx][ny][crush] = 1
                    # 다음 이동할 노드가 길이라면
                    if graph[nx][ny] == 0:
                        queue.append((nx, ny, crush, cnt + 1))
                    # 다음 이동할 좌표가 벽이라면
                    else:
                        # 벽인데 그전에 다른벽을 부순적이 없다면
                        if not crush:
                            queue.append((nx, ny, crush + 1, cnt + 1))
 
    return possible

if BFS(0, 0):
    print(min(answer))
else:
    print(-1)
