from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(priority, key) for (key, priority) in enumerate(priorities)])   # 우선순위값과 프로세스번호(인덱스)를 튜플로 묶어 큐에 삽입.
 

    # 큐가 남아있을 동안 pop은 계속됨.
    while queue:
        curPriority, curKey = queue.popleft()   # (우선순위, 프로세스번호)를 pop함.
        
        # cur와 배열안의 나머지숫자들과 비교.
        if all(curPriority >= item for (item, key) in queue):
            answer += 1
            # 알고싶은 위치의 프로세스 넘버라면 return.
            if curKey == location:
                return answer
        else:
            queue.append((curPriority, curKey))
    
# location에 해당하는 프로세스가 언제 실행되는지 알고싶은거임.
# priorities에 있는 숫자들은 말그래도 각 프로세스의 우선순위를 의미.
# 프로세스 번호는 priorities의 인덱스 번호라고 하자.
# 그럼 큐에 저장을 할때 (key, value) 형태로 저장하면 좋겠지?
# => key = 인덱스번호, value = 우선순위값

# [1, 1, 9, 1, 1, 1]
# => [C, D, E, F, A, B]