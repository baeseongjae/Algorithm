import sys

input = sys.stdin.readline
N = int(input())
arr = [[0, 0] for _ in range(N)]
answer = 0

for i in range(N):
    arr[i][0], arr[i][1] = map(int, input().split())

arr.sort(key=lambda x: (x[1], x[0]))

prev = arr[0][1]
answer = 1
for i in range(1, N):
    # 이전 강의시간의 종료시간보다 나중에 시작한다면
    if arr[i][0] >= prev:
        prev = arr[i][1]
        answer += 1
print(answer)