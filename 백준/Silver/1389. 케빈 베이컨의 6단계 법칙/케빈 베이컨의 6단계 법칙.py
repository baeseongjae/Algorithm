import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[float('inf') for _ in range(N+1)]  for _ in range(N+1)]
kev = []
answer = []

# A와 B가 같은 비용은 없다 했으므로 자기 자신으로 가는 비용은 0
for a in range(N+1):
    for b in range(N+1):
        if a == b:
            matrix[a][b] = 0
        if a == 0 or b == 0:
            matrix[a][b] = 0

# 입력값 받아서 해당 행렬 원소 1로 만들기.
for _ in range(M):
    n1, n2 = map(int, input().split())
    # 중복되어 들어올 수 있으므로
    
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

def floydWarshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
                        

def kevinBacon():
    floydWarshall()

    # 그래프의 행에 속한 원소들의 합을 kev리스트에 삽입.
    for row in matrix:
        kev.append(sum(row))    

    # 최솟값 구할 것이므로 0번째 인덱스는 다시 무한대 수로 수정.
    kev[0] = float('inf')
    minValue = min(kev)

    # 케빈베이컨 수가 가장 적은 사람을 고르는 로직
    for index, value in enumerate(kev):
        if value == minValue:
            answer.append(index)

    print(min(answer))

kevinBacon()