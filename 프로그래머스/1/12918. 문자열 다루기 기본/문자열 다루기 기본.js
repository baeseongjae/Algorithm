function solution(s) {
    let answer = true;

    // 길이 검사 / 숫자로만 구성됐는지 검사
    return s.length === 4 || s.length === 6 ? (s == parseInt(s) ? true : false) : false;
}