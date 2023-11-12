T = int(input())

def solution(tc):
    N = int(input())
    D = [[0 for _ in range(N)] for _ in range(N)]

    D[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            # 맨 왼쪽 원소
            if j == 0:
                D[i][j] = D[i-1][0]
            # 맨 오른쪽 원소
            elif j == N-1:
                D[i][j] = D[i-1][0]
            elif 1 <= j < N-1:
                D[i][j] = D[i-1][j-1] + D[i-1][j]

    print('#' + str(tc))
    for i in range(N):
        for j in range(i+1):
            print(D[i][j], end=' ')
        print()

for i in range(1, T+1):
    solution(i)