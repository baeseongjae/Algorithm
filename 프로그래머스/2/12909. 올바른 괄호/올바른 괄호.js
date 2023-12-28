// function solution(s){
//     var answer = true;
//     let stackCnt = 0;

//     for (let i = 0; i < s.length ; i++) {
//         if (s[i] === "(") {
//             stackCnt++;
//         }   else if (s[i] === ")") {
//             if (stackCnt <= 0) {
//                 answer = false;
//                 break;
//             }
//             stackCnt--;
//         }
//     }
//     if (stackCnt !== 0) answer = false;
    
//     return answer;
// }






function solution(s) {
    answer = true;
    stack = [];
    
    for (let x of s) {
        if (x === '(') {
            stack.push(x);
        } else if (x === ')') {
            // 스택에 아이템이 있으면 팝
            if (stack.length) {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    if (stack.length) {
        return false;
    }
    // 괄호 짝이 맞아야 한다.
    // 근데 ( 이게 먼저 나와야한다.
    // (()(
    // 스택을 사용해서 스택에 내용이 없으면 true
    
    return answer;
}