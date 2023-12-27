from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(priority, key) for (key, priority) in enumerate(priorities)])   # 우선순위값과 프로세스번호(인덱스)를 튜플로 묶어 큐에 삽입.
 
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