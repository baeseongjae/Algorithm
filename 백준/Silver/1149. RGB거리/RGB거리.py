N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [[0 for _ in range(N)] for _ in range(N)]

# D[i] : i번째 집까지 누적된 최소비용을 색상별로 메모한 리스트
# D[i][0] - 빨강,  D[i][1] - 초록, D[i][2] - 파랑
D[0][0] = arr[0][0]
D[0][1] = arr[0][1]
D[0][2] = arr[0][2]

for i in range(1, N):
    D[i][0] = arr[i][0] + min(D[i-1][1], D[i-1][2])  # 빨간색
    D[i][1] = arr[i][1] + min(D[i-1][0], D[i-1][2])  # 초록색
    D[i][2] = arr[i][2] + min(D[i-1][0], D[i-1][1])  # 파란색

print(min(D[N-1][0], D[N-1][1], D[N-1][2]))
# 점화식 
# D[n][색상1] = arr[n][색상1] + min(D[n-1][색상2], D[n-1][색상3])