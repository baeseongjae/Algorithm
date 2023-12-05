N, K = map(int, input().split())
arr = []
answer = 0

for i in range(N):
    data = int(input())
    arr.append(data)

for i in range(N-1, -1, -1):
    if K >= i:
        answer += K // arr[i]
        K %= arr[i]
print(answer)
