function solution(people, limit) {
    let answer = 0;
    let start = 0;
    let end = people.length - 1;
    
    // 1. 먼저 몸무게 큰 순으로 정렬 
    // 2. 두명의 몸무게의 합이 구명보트보다 작으면 통과 및 양쪽 포인터 이동
    // 3. 크다면, start 포인터를 증가?
    
    people.sort((a, b) => b - a)
    
    while (start <= end) {
        if (start === end) 
            return ++answer;
        
        if (people[start] + people[end] <= limit) {
            start += 1;
            end -= 1;
        } else {
            start += 1;
        }
        answer += 1 
    }
    
    return answer;
}