T = int(input())

for _ in range(T):
    N = int(input())
    D = [0] * 101
    for i in range(3):
        D[i] = 1
    
    for i in range(3, N):
        D[i] = D[i-3] + D[i-2]
    
    print(D[N-1])