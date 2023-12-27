function solution(citations) {
    let answer = 0;
    let n = citations.length;
    
    citations.sort((a, b) => b - a);    //내림차순 정렬
  
    // i    0 1 2 3 4
    // c[i] 6 5 3 1 0
    
    for (let i = 0; i < n; i++) {
        if (i >= citations[i]) {
            answer = i
            return answer
        }
    }
    
    return n
}