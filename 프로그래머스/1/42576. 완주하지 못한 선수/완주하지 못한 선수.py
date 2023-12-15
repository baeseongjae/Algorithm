def solution(participant, completion):
    answer = ''
    myDict = {}
    
    for item in participant:
        if item not in myDict: 
            myDict[item] = 1
        else:
            myDict[item] += 1
            
    for item in completion:
        if item in myDict:
            myDict[item] -= 1
    
    answerArr = [item for item in myDict if myDict[item] == 1]
    answer = answerArr[0]
    
    return answer