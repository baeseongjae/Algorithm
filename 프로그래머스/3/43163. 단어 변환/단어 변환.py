from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0] * (len(words))
    
    def BFS(data):
        # 한글자씩 탐색? 
        queue = deque([[data, 0]]) # 단어, 변환횟수
        
        while queue:
            data, cnt = queue.popleft()
            
            if data == target:
                return cnt
            
            # words 배열의 단어중 한개만 변환하여 바꿀 수 있는 단어 탐색
            for i in range(len(words)):
                # 방문안한것중에서 탐색
                if not visited[i]:
                    check = 0
                    for j in range(len(words[i])):
                        # 다른 문자가 하나여야만 하므로
                        if data[j] != words[i][j]:
                            check += 1
                    if check == 1:
                        queue.append([words[i], cnt+1])
                        visited[i] = 1
        
        return 0
    
    answer = BFS(begin)
    
    return answer