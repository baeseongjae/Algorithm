import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
tmpArr = [1,2,3,14]
visited = [False]*(n+1)

def DFS(node):    # DFS 함수
    visited[node] = True
    for v in arr[node]:
        if not visited[v]:  # 인접리스트 노드가 방문하지 않았을때 즉, visited[v] = False일 경우            
            DFS(v)
    
for _ in range(m): # m번 반복하면서 그래프 데이터 2차원 배열(인접리스트)에 저장
    start,end = map(int,input().split())
    arr[start].append(end)
    arr[end].append(start)

cnt = 0

for i in range(1,n+1):
    if visited[i]==False:
        cnt+=1
        DFS(i)

print(cnt)