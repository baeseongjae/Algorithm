from collections import deque

N, K = map(int, input().split())
M = 100000
dist = [-1] * (M+1)

def BFS(start):
    queue = deque([start])
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        if cur == K:
            return

        for next in (cur-1, cur+1, cur*2):
            # 범위 안에 있고
            if 0 <= next <= M:
                # 방문하지 않았다면
                if dist[next] == -1:
                    # 순간이동이라면
                    queue.append(next)
                    if next == cur*2:
                        dist[next] = dist[cur]
                    else:
                        dist[next] = dist[cur] + 1
                # 방문한 노드라면 최솟값 비교
                else:
                    if next == cur*2:
                        dist[next] = min(dist[next], dist[cur])
                    else:
                        dist[next] = min(dist[next], dist[cur] + 1)
BFS(N)
print(dist[K])