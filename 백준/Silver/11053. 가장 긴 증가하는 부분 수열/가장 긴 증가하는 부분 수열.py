N = int(input())
arr = list(map(int, input().split()))
D = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            D[i] = max(D[i], D[j] + 1)

print(max(D))