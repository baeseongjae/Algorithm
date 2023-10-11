N = int(input())

D = [[0 for _ in range(10)] for _ in range(N+1)]
mod = 1000000000

for h in range(1, 10):
    D[1][h] = 1

for i in range(2, N+1):
    D[i][0] = D[i-1][1]   # h가 0일때
    D[i][9] = D[i-1][8]   # h가 9일때
    for h in range(1, 9):
        D[i][h] = D[i-1][h-1] + D[i-1][h+1]

answer = sum(D[N]) % mod

print(answer)