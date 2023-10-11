N = int(input())
D = [[0 for i in range(10)] for _ in range(N)]
answer = 0

for i in range(10):
    D[0][i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(j, 10):
            D[i][k] = (D[i][k] + D[i-1][j]) % 10007

for i in range(10):
    answer = (answer + D[N-1][i]) % 10007

print(answer)
