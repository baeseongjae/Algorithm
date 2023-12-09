import sys
input = sys.stdin.readline

#전역 변수 선언
checkList = [0]*4   # 비밀번호 체크 리스트
curList = [0]*4     # 현재 체크 상태 리스트
checkPw = 0         # 몇개의 문자 조건 충족했는지 나타내는 변수
result = 0          # 모든조건을 충족하여 만들수 있는 비밀번호 종류 개수

s, p = map(int,input().split())
str = list(input())
checkList = list(map(int,input().split()))

def addNew(c):
    global checkList, curList, checkPw
    if c == 'A':
        curList[0]+=1
        if curList[0]==checkList[0]:
            checkPw +=1
    elif c == 'C':
        curList[1]+=1
        if curList[1]==checkList[1]:
            checkPw +=1
    elif c == 'G':
        curList[2]+=1
        if curList[2]==checkList[2]:
            checkPw +=1
    elif c == 'T':
        curList[3]+=1
        if curList[3]==checkList[3]:
            checkPw +=1


def removeBefore(c):
    global checkList, curList, checkPw
    if c == 'A':
        if curList[0]==checkList[0]:
            checkPw -=1
        curList[0]-=1
    elif c == 'C':
        if curList[1]==checkList[1]:
            checkPw -=1
        curList[1]-=1
    elif c == 'G':
        if curList[2]==checkList[2]:
            checkPw -=1
        curList[2]-=1
    elif c == 'T':
        if curList[3]==checkList[3]:
            checkPw -=1
        curList[3]-=1

for i in range(4):
    if checkList[i]==0:
        checkPw+=1


for i in range(p):
    addNew(str[i])

if checkPw == 4:
    result+=1

for i in range(p,s):
    j = i-p
    # 슬라이딩 윈도우 한칸씩 이동하면서 추가된 오른쪽 끝원소 더하고, 왼쪽 끝원소 뺌.
    # 더하는 로직 또 작성해야하네?
    # 그럼 더하고 빼는 로직을 함수로 따로 만들면 더 좋겠지?
    addNew(str[i])
    removeBefore(str[j])
    if checkPw == 4:
        result+=1

print(result)

#문제핵심
#비밀번호 유효성 검사시, 기존 검사결과 체크리스트에
#새로 들어온 문자열, 제거되는 문자열을 반영하여 확인하는것이 핵심.