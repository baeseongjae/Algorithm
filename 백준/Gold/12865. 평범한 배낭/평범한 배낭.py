N, K = map(int, input().split())
D = [[0 for _ in range(K+1)] for _ in range(N)]
W = [0] * N
V = [0] * N
tmp = 0

for i in range(N):
    w, v = map(int, input().split())
    W[i] = w
    V[i] = v

for j in range(W[0], K+1):
    D[0][j] = V[0]

for i in range(1, N):
    for j in range(1, K+1):
        if j - W[i] >= 0:
            # 배낭에 물건 더 넣을 수 있을때
            D[i][j] = max(D[i-1][j-W[i]] + V[i], D[i-1][j])
        # 없을때
        else:
            D[i][j] = D[i-1][j]
print(D[N-1][K])