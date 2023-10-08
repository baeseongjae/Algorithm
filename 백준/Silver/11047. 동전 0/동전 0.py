N, K = map(int, input().split())
arr = [0] * N
cnt = 0

for i in range(N):
    arr[i] = int(input())

for i in range(N-1, -1, -1):
    if K >= arr[i]:
        cnt += (K // arr[i])
        K %= arr[i]

print(cnt)