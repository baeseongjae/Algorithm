from collections import deque

N = int(input())
K = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, -1, 0, 1]  # 각각 우 상 좌 하
dy = [1, 0, -1, 0]
directions = {}

# 입력값1) 사과 위치 정보 저장
for i in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

L = int(input())
# 입력값2) 방향 변환 정보 저장
for i in range(L):
    x, d = input().split()
    directions[int(x)] = d

def rotateDir(index, str):  # 방향 나타내는 인덱스, 방향
    # 상3 하2 좌1 우0
    # L 왼쪽회전 => 우 -> 상(1) -> 좌(2) -> 하(3)
    # D 오른쪽회전 => 우(0) -> 하(3) -> 좌(2) -> 상(1)
    if str == 'L':
        result = (index + 1) % 4
    elif str == 'D':
        result = (index + 3) % 4
    return result

def start(x, y):
    dir = 0 # 처음은 오른쪽으로 향하니, 동을 나타내는 인덱스0 에 접근 위해 설정.
    queue = deque([(x, y)])
    arr[x][y] = 2
    time = 0
    
    while True:
        time += 1
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 범위안에 있고 방문한 지역 아니라면
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 2:
            queue.append((nx, ny))
            x, y = nx, ny
            # 사과가 있다면 꼬리 안뺌 그대로 늘림.
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2   # 방문
            else:
                arr[nx][ny] = 2
                px, py = queue.popleft()
                arr[px][py] = 0
        else:
            break

        if time in directions.keys():
            dir = rotateDir(dir, directions[time])
    
    return time

print(start(0, 0))