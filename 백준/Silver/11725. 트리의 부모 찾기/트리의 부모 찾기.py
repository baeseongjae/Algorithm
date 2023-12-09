import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)   #부모노드 저장

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def DFS(start):
    visited[start] = True
    for node in tree[start]:
        if not visited[node]:
            answer[node] = start
            DFS(node)

DFS(1)

for i in range(2, N+1):
    print(answer[i])