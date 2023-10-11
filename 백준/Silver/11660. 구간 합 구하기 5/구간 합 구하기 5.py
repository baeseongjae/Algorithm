import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

# 원본배열 채우기
for i in range(n):
    arrRow = [0] + [int(x) for x in input().split()]
    arr.append(arrRow)

# 합배열 채우기
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + arr[i][j]

# 질의에 대한 답 구현코드
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    answer = D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]
    print(answer)