import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1) # 거리정보 저장, dist[x] = x위치에 오기까지 걸린 시간

def BFS():
    queue = deque()
    queue.append(N)

    while queue:
        cur = queue.popleft()

        if cur == K:
            print(dist[K])
            return

        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= MAX and not dist[next]:
                queue.append(next)
                dist[next] = dist[cur] + 1

BFS()