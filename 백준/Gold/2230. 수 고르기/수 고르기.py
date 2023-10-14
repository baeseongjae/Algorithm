import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

A.sort()

i = 0
j = 1
cnt = 0
answer = []

# 투포인터 활용
while j < N:
    if A[j] - A[i] >= M:
        answer.append(A[j]-A[i])
        i += 1
        j += 1
        if j - i > 1:
            j -= 1
    # 차이가 M보다 작다면
    else:
        j += 1
    
print(min(answer))    