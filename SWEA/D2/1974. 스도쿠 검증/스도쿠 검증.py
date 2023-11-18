T = int(input())
def isSectionValid(arr):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # 각 섹션 안에서 검사
            sectionNum = [0] * 10
            for r in range(3):
                for c in range(3):
                    cur = arr[i+r][j+c]
                    # 같은숫자가 있다면 0반환
                    if sectionNum[cur]:
                        return 0
                    sectionNum[cur] = 1
    return 1

def isRowValid(arr):
    for i in range(9):
        rowNum = [0] * 10
        for j in range(9):
            cur = arr[i][j]
            if rowNum[cur]:
                return 0
            rowNum[cur] = 1
    return 1

def isColumnValid(arr):
    for j in range(9):
        columnNum = [0] * 10
        for i in range(9):
            cur = arr[i][j]
            if columnNum[cur]:
                return 0
            columnNum[cur] = 1
    return 1

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    r = isRowValid(arr)
    c = isColumnValid(arr)
    s = isSectionValid(arr)

    if r and c and s:
        answer = 1
    else:
        answer = 0

    print(f"#{test_case} {answer}")

# 확인해야할것
# 3*3 격자로 나눠서 같은숫자가 있는지 확인하는 로직
# 같은 세로줄, 가로줄 확인 로직