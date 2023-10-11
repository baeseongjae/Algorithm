N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [1] * N


# 오름차순 정렬
arr = sorted(arr, key = lambda x: x[0])

# LIS 어떻게 활용할지 생각
for i in range(1, N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            D[i] = max(D[i], D[j] + 1)

print(N - max(D))