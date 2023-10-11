import sys, math

# 입력부
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
val = sum(arr)

# dp : 현재 i번째 추에서 무게 j를 만들 수 있는지 아닌지를 나타내는 상태 공간
dp = [[False] * (val + 1) for _ in range(n)]

# 무게 0과 첫번째 추의 무게는 무조건 만들 수 있다
dp[0][0] = True
dp[0][arr[0]] = True

# 점화식
for i in range(1, n):
    for j in range(val + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
            dp[i][j + arr[i]] = True
            
# check : 만들 수 있는 무게들의 집합
check = set()
for i in range(n):
    for j in range(val + 1):
        if dp[i][j]:
            check.add(j)
            
# 입력부
m = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
for i in temp:
    find = False
    for j in check:
        # 무게의 차가 구슬의 무게만큼이라면 가능
        if j - i in check:
            find = True
            break
    # find의 여부에 따라 정답 출력
    print('Y' if find else 'N', end=' ')