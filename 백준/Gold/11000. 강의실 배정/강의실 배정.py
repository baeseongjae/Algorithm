import heapq
import sys

input = sys.stdin.readline
N = int(input())
arr = [[0, 0] for _ in range(N)]
answer = 0 # 강의실 수
heap = []

for i in range(N):
    arr[i][0], arr[i][1] = map(int, input().split())

arr.sort(key=lambda x: x[0])
heapq.heappush(heap, arr[0][1]) # 첫 강의 끝나는 시간
for i in range(1, N):
    # heap[0] 가장 빨리끝나는 강의실임.
    # 다음 강의 시작시간이 더 작으면, 강의실 늘려야하므로
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    # 아니라면, 같은 강의실에서 가능
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))