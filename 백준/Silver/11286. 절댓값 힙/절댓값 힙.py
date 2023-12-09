import heapq
import sys

input = sys.stdin.readline
heap = []
N = int(input())

for i in range(N):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))