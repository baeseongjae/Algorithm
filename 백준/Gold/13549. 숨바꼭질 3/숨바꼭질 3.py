from collections import deque
N, K = map(int, input().split())
M = 100000
dist = [-1] * (M+1)

def BFS(cur):
    queue = deque([cur])
    dist[cur] = 0
    
    while queue:
        cur = queue.popleft()

        if cur == K:
            return dist[cur]

        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= M:
                if dist[next] == -1:
                    if next == cur*2:
                        dist[next] = dist[cur]
                    else:
                        dist[next] = dist[cur] + 1
                    queue.append(next)

                # 방문했었다면
                else:
                    if next == cur*2:
                        dist[next] = min(dist[next], dist[cur])
                    else:
                        dist[next] = min(dist[next], dist[cur] + 1)
                
print(BFS(N))
