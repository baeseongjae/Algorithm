def solution(sizes):
    answer = 0
    
    # 가장 큰 w, h중에 큰거를 한 변으로
    # 가장 작은 w, h중에 큰거를 한 변으로
    answer = max(max(item) for item in sizes) * max(min(item) for item in sizes)
    
    # 모든 명함을 수납할수있는 최소넓이를 구하자.
    return answer