import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    grade = [[0, 0] for _ in range(N)]
    answer = 0
    for i in range(N):
        grade[i][0], grade[i][1] = map(int, input().split())
    
    sortedArr = sorted(grade, key=lambda x: x[0])

    answer = 1
    minValue = sortedArr[0][1]
    for i in range(1, N):
        # 서류기준으로 오름차순 정렬된 상태이므로
        # 면접성적이 더 높아야 즉, 값이 더 낮으면 합격
        if sortedArr[i][1] < minValue:
            minValue = sortedArr[i][1]
            answer += 1
    
    print(answer)