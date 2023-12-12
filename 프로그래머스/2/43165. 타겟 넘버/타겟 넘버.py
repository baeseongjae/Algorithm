def solution(numbers, target):
    answer = 0
    num = 0

    def DFS(depth, tot):
        if depth == len(numbers):
            if tot == target:
                return 1
            return 0
        
        res = 0
        res += DFS(depth+1, tot+numbers[depth])
        res += DFS(depth+1, tot-numbers[depth])
        
        return res
    
    answer = DFS(0, 0)
    return answer


    
    