N = int(input())
arr = [0] * (N+1)
D = [0] * (N+1)
for i in range(1, N+1):
    data = int(input())
    arr[i] = data

# 계단이 2개이하인 경우
if N <= 2:
    print(sum(arr))

# 계단이 3개이상인 경우 (세개 연속해서 못밟으므로)
else:
    D[1] = arr[1]
    D[2] = arr[1] + arr[2]
    for i in range(3, N+1):
        D[i] = max(D[i-3]+arr[i-1]+arr[i], D[i-2]+arr[i])
    print(D[N])
