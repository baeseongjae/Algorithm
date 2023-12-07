from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = []

for i in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)

# 시작노드 부터 완전탐색
def BFS(node):
    depth = 0
    queue = deque([node])
    visited[node] = 1 

    while queue:
        v = queue.popleft()

        for next in graph[v]:
            if not visited[next]:
                depth += 1
                queue.append(next)
                visited[next] = 1
                
    return depth

maxValue = 0
# cnt 가장 큰 컴퓨터번호 찾기.
for i in range(1, N+1):
    visited = [0] * (N+1)
    cnt = BFS(i)

    if cnt > maxValue:
        maxValue = cnt
        answer = []
        answer.append(i)
    elif cnt == maxValue:
        answer.append(i)

print(*answer)

# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터는?
# 모든 컴퓨터를 시작점으로 완전탐색 시행하여 총 뎁스 파악 => 가장 큰거 골라서 배열삽입 후 출력.