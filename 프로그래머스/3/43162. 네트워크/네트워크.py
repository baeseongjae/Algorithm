from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    queue = deque()
    
    def BFS(node):
        queue.append(node)
        visited[node] = 1
        while queue:
            v = queue.popleft()
                
            for nv in range(n):
                if computers[v][nv] == 1 and not visited[nv]:
                    queue.append(nv)
                    visited[nv] = 1
    
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
            
    return answer