function solution(array, commands) {
    let answer = [];
    
    for(let item of commands) {
        [i, j, k] = item;
        let list = array.slice(i-1, j).sort((a, b) => a - b);
        answer.push(list[k-1])
    }
    
    return answer;
}
