function solution(s){
    var answer = true;
    let stackCnt = 0;

    for (let i = 0; i < s.length ; i++) {
        if (s[i] === "(") {
            stackCnt++;
        }   else if (s[i] === ")") {
            if (stackCnt <= 0) {
                answer = false;
                break;
            }
            stackCnt--;
        }
    }
    if (stackCnt !== 0) answer = false;
    
    return answer;
}