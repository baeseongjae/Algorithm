def solution(citations):
    answer = 0
    n = len(citations)
    
    citations.sort(reverse=True);
    
    for i in range(n):
        if i >= citations[i]:
            return i
    
    # h번 이상 인용된 논문이 h편이상, 나머지가 h번 이하 인용
    
    # citations 발표한 논문의 인용횟수 들이 담긴 배열
    # len(citations) 발표 논문 수
    
    return n