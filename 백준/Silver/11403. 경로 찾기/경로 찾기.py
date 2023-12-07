
# 왜 범위를 1부터 N까지 지정하면 인덱스 참조에러 나는지 모르겠네.
# N = int(input())

# arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     arr[i] = list(map(int, input().split()))
    
# def floydWarshall(graph):
#     for k in range(1, N+1):
#         for i in range(1, N+1):
#             for j in range(1, N+1):
#                 if graph[i][k] == 1 and graph[k][j] == 1:
#                     graph[i][j] = 1


# floydWarshall(arr)

# print(*arr)


N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))
    
def floydWarshall(graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1


floydWarshall(arr)

for i in range(N):
    print(*arr[i])