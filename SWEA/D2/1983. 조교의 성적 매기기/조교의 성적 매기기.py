T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    grade = 0
    gradeDict = {}
    for i in range(N):
        grade = (arr[i][0] * 0.35) + (arr[i][1] * 0.45) + (arr[i][2] * 0.2)
        gradeDict[i] = grade

    # 안의 튜플을 리스트로 변환
    sortedArr = [[k, v] for k, v in sorted(gradeDict.items(), key=lambda x: -x[1])]

    tmp = N // 10
    cnt = 0
    j = 0
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        sortedArr[i].append(score[j])
        cnt += 1
        if tmp == cnt:
            j += 1
            cnt = 0

    sortedArr.sort(key=lambda x: x[0])

    answer = sortedArr[K-1][2]

    print(f"#{tc} {answer}")

# 각각의 성적을 합산해서 딕셔너리? 만들기 오름차순