from collections import deque

N, K = map(int, input().split())
M = 100000
dist = [[-1, -1] for i in range(M+1)]
path = []

def BFS(start):
    queue = deque([start])
    dist[start][0] = 0

    while queue:
        cur = queue.popleft()

        if cur == K:
            print(dist[K][0])
            while cur != -1:
                path.append(cur)
                cur = dist[cur][1]
            for i in range(len(path)-1, -1, -1):
                print(path[i], end=' ')

        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= M:
                # 방문안한 노드라면 
                if dist[next][0] == -1:                
                    queue.append(next)
                    dist[next][0] = dist[cur][0] + 1
                    dist[next][1] = cur

BFS(N)