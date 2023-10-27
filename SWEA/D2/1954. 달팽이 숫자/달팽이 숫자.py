#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    dx = [0, 1, 0, -1] # (동, 남, 서, 북)
    dy = [1, 0, -1, 0]
    dir = 0
    r, c = 0, 0

    for num in range(1, N*N+1):
        # 숫자 삽입
        arr[r][c] = num
        # 이동
        r += dx[dir]
        c += dy[dir]

        # 해당 지역이 범위를 벗어났거나 이미 값이 있다면
        if r < 0 or r >= N or c < 0 or c >= N or arr[r][c]:
            # 이전상태로 다시이동 
            r -= dx[dir]
            c -= dy[dir]

            # 방향 바꾸기(동->남, 남->서, 서->북, 북 >동)
            dir = (dir + 1) % 4

            # 이동
            r += dx[dir]
            c += dy[dir]

    print('#' + str(tc))
    for row in arr:
        print(*row)