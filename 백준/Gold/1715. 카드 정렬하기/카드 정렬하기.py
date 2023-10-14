import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []
answer = []

for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

if N == 1:
    answer.append(0)
else:
    while True:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        answer.append(a+b)
        if not heap:
            break
        heapq.heappush(heap, a+b)

print(sum(answer))
