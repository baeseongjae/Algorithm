N = int(input())
D = [0] * N
arr = [int(input()) for _ in range(N)]

if N < 3:
    print(sum(arr))
else:
    D[0] = arr[0]
    D[1] = arr[0] + arr[1]
    D[2] = max(arr[0]+arr[2], arr[1]+arr[2], D[1])
    for i in range(3, N):
        D[i] = max(D[i-2]+arr[i], D[i-3]+arr[i-1]+arr[i], D[i-1])
    
    print(D[N-1])