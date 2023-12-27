function solution(priorities, location) {
    let queue = priorities.map((priority, index) => ({ priority, index}));
    let answer = 0;
    
    while (queue.length) {
        let cur = queue.shift();
        
        // 현재 프로세스의 우선순위가 더 작은게 있다면 현재프로세스는 다시 큐에 삽입
        if (queue.some(item => item.priority > cur.priority)) {
            queue.push(cur);
        } else {
            answer += 1
            if (cur.index === location) {
                return answer;
            }
        }
    }
    
}