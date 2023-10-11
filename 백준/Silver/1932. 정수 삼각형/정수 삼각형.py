N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [[0 for j in range(len(arr[i]))] for i in range(N)]

D[0] = arr[0]

# DP 트리 채우기
for i in range(1, N):
    M = len(arr[i])
    for j in range(M):
        if 0 < j < M-1:
            D[i][j] = arr[i][j] + max(D[i-1][j-1], D[i-1][j])
        elif j == M-1:
            D[i][j] = arr[i][j] + D[i-1][j-1]
        elif j == 0:
            D[i][j] = arr[i][j] + D[i-1][j]

# N-1번째 dp리스트에 있는 리스트에서 최댓값 구하면 됨.
print(max(D[N-1]))