import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 2 for _ in range(N)]
end = arr[0][1]
cnt = 0

for i in range(N):
    s, e = map(int, input().split())
    arr[i][0] = s
    arr[i][1] = e
    
# 종료시간이 빠른 순서대로 정렬
# 종료시간이 같을 경우 시작시간이 빠른순으로 정렬하는 로직도 추가해야함
arr.sort(key=lambda arr: (arr[1], arr[0]))

for i in range(N):
    if arr[i][0] >= end:
        end = arr[i][1]
        cnt += 1

print(cnt)