import sys
from collections import deque

def BFS():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        curX, curY = queue.popleft()
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[curX][curY] + 1
                queue.append((nx, ny))

if __name__ == "__main__":
    input = sys.stdin.readline
    M, N = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    # 입력값 저장
    for i in range(N):
        graph[i] = list(map(int, input().split()))
    
    queue = deque()

    # 처음에 1이 적혀있는 좌표중 하나를 골라 탐색해야할듯.
    # 익은 토마토의 인접한 곳이 익게 되는 것이 조건이므로 
    # 1이 있는 좌표 전부 다 큐에 삽입.
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))   

    # BFS 실행 (토마토 익히기)
    BFS()

    # 최소 경과일 수는 과일이 다 익었을 시점의
    # 좌표 인덱스에 저장된 값 출력하면 되니까 배열의 최댓값.
    answer = 0
    for row in graph:
        for item in row:
            # item이 0 인게 하나라도 있으면 모두 익지 못하는 상황.
            if item == 0:
                print(-1)
                exit()
        # 0이 있는지 검사 끝났으면, sub배열의 최댓값 업데이트.
        answer = max(answer, max(row))

    # 1에서부터 카운트 시작했으므로 
    # 경과 일수를 출력하려면 1빼야함
    print(answer - 1)