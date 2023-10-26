T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for r in range(M):
                for c in range(M):
                    total += arr[r+i][c+j]
            
            if answer < total:
                answer = total 

    print('#' + str(tc+1), end=' ')
    print(answer)