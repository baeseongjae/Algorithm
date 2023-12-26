# array = []
# commands = [[],[],[]]

def solution(array, commands):
    answer = []
    for row in commands:
        i, j, k = row
        
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer