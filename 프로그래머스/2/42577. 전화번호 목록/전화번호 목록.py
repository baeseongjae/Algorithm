def solution(phone_book):
    answer = True
    myDict =  {}
    
    for item in phone_book:
        myDict[item] = 1

    for item in phone_book:
        part = ""
        for num in item:
            part += num # 문자를 더해가며 부분문자열 생성
            if part in myDict and part != item:
                return False
    # 1. 폰북 배열 속 원소를 key로 하는 myDict 키,값 생성.
    # 2. 폰북 속을 탐색하며 item 마다 각 item의 문자를 부분문자열로 하는 부분문자열 생성.
    # 3. 그리고 그 부분 문자열이 myDict의 key로 속해있는지 검사
    # 4. 자기자신이 아닌지 검사
    # 5. 조건문 하나라도 충족하면 False값 반환
    return answer