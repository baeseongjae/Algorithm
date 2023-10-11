N = int(input())
arr = [0] * (N+1)
D = [0] * (N+1)
answer = 0

for i in range(1, N+1):
    arr[i] = int(input())

if N <= 2:
    answer = sum(arr)
else:
    D[1] = arr[1]
    D[2] = arr[1] + arr[2]

    for i in range(3, N+1):
        D[i] = max(D[i-2]+arr[i], D[i-3]+arr[i-1]+arr[i])
    answer = D[N]

print(answer)
