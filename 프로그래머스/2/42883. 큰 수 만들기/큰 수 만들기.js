function solution(number, k) {
    let answer = '';
    // 스택 활용
    // (스택 맨 위에 있는 값 < push 예정값) 이라면, 크거나 같은값이 나올때까지 pop 
    let stack = [];
    
    for(let x of number) {    
        while (k > 0 && stack && stack[stack.length-1] < x) {
            stack.pop();
            k -= 1;
        }
        stack.push(x)
    }
    
    //아직 제거할 숫자 (k)가 남았을경우
    
    while (k > 0) {
        stack.pop();
        k -= 1;
    }
    
    return stack.join('');
}