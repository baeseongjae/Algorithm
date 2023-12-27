function solution(numbers) {
    var answer = '';
    
    stringArr = numbers.map(item => String(item));
    answer = stringArr.sort((a, b) => (b + a) - (a + b)).join('');
    
    return answer[0] === "0" ? "0" : answer;
}