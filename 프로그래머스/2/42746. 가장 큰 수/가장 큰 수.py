def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(key=lambda x: x*3, reverse=True)
    
    for item in numbers:
        answer += item
        
    # 순서 재배치하여 만들 수 있는 가장 큰수 구하기
    # 요구사항
    # 1. 숫자가 큰 아이템부터 배치.
    # 2. 숫자가 두자리 수 이상이라면 맨 앞자리부터 비교하여 큰 숫자 부터 배치
    # 3. 한자리수와 두자리수이상의 숫자를 비교할때 같은 방식으로 비교하되,
    #    한자리수가 두자리수이상숫자의 각자릿수 숫자들 보다 한개라도 더 큰게 있다면  (예를 들어 3 vs 30)
    #    한자리수를 먼저 배치.
    
    
    return str(int(answer))