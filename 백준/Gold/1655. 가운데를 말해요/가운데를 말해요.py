import sys
import heapq

input = sys.stdin.readline
N = int(input())
leftHeap = []
rightHeap = []

for i in range(N):
    data = int(input())

    if len(leftHeap) == len(rightHeap):
        # 최대힙으로 구현
        heapq.heappush(leftHeap, -data)
    else:
        # 최소힙으로 구현
        heapq.heappush(rightHeap, data)

    # 
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        l = heapq.heappop(leftHeap)
        r = heapq.heappop(rightHeap)

        heapq.heappush(rightHeap, -l)
        heapq.heappush(leftHeap, -r)        

    print(-leftHeap[0])