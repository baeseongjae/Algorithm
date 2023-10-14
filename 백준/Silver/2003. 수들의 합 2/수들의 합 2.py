N, M = map(int,input().split())
A = list(map(int, input().split()))
i = 0
j = 0
cnt = 0

while i < N and j < N:
    # A[i]와 A[j]합을 구해 M보다 작으면 j값 증가, 크면 i값증가, 같으면 cnt += 1
    testSum = sum(A[i:j+1])

    if testSum < M:
        j += 1
    elif testSum > M:
        i += 1
    else:
        cnt += 1 
        j += 1

print(cnt)