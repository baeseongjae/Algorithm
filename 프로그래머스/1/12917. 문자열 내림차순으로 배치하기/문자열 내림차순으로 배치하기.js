function solution(s) {
    let answer = '';
    const arr = s.split("")
    
    answer = arr.sort().reverse().join("");
    
    
    return answer;
}