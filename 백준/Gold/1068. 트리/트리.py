import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
visited = [False] * (N)
parentNode = list(map(int, input().split()))

# 받은 입력값들로 Tree 데이터 구현.
for pIndex, pValue in enumerate(parentNode):
    if pValue == -1:
        root = pIndex
        continue
    else:
        tree[pValue].append(pIndex)

# 트리 데이터 검증
# print(tree) 

delNode = int(input())
leafCnt = 0

def DFS(start):
    global leafCnt
    visited[start] = True
    subNode = 0
    
    # start와 연결된 노드 탐색
    for node in tree[start]:
        # 삭제할 노드라면, 해당 노드의 서브트리데이터 모두 탐색중지
        if not visited[node] and node != delNode:
            subNode += 1
            DFS(node)

    if subNode == 0:
        leafCnt += 1
        
if delNode == root:
    print(0)
else:
    DFS(root)
    print(leafCnt)