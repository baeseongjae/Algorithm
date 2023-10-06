from collections import deque

N, K = map(int, input().split())
M = 100000
dist = [[-1, 0] for _ in range(M+1)] #첫번째 인덱스는 최소시간을 의미, 두번째는 최소시간으로 도달하는 방법수를 의미

def BFS(start):
    queue = deque([start])
    dist[start] = [0, 1]

    while queue:
        cur = queue.popleft()

        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= M:
                # 이전에 방문한 노드가 아니라면
                if dist[next][0] == -1:
                    queue.append(next)
                    dist[next] = [dist[cur][0] + 1, dist[cur][1]]
                # 이미 방문한적이 있다면, 더 최소시간으로 갱신
                else:
                    # 방문할 노드의 최소시간과 이미 저장된 최소시간이 같다면 방법수 1증가
                    if dist[next][0] == dist[cur][0] + 1:
                        dist[next][1] += dist[cur][1]
                    dist[next][0] = min(dist[next][0], dist[cur][0] + 1)
                    

BFS(N)
print(dist[K][0])
print(dist[K][1])