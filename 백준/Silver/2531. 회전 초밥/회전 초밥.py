import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())  # d는 초밥가짓수, k는 연속으로 먹는 접시수
arr = [int(input()) for _ in range(N)]  # 배열에 입력값 받기 (초밥번호)
dict = {}  # 초밥 개수 저장할 딕셔너리
maxValue = 0
l = 0
r = l + (k-1)

# 회전하므로 리스트 두개를 잇는다
# 7 9 7 30 2 7 9 25 / 7 9 7 30 2 7 9 25
arr.extend(arr)

# 4개 연속으로 먹을거니까, 쿠폰번호 초밥 받음
dict[c] = 1

# 초기 윈도우에서 초밥 종류 세자.
for i in range(l, r+1):
    if arr[i] not in dict:
        dict[arr[i]] = 1
    else:
        dict[arr[i]] += 1

# 먹은 초밥 가짓수 세기
maxValue = len(dict)

r += 1

# 슬라이딩 윈도우 적용
while r < len(arr):
    # 맨 왼쪽 초밥 제거
    dict[arr[l]] -= 1
    if dict[arr[l]] == 0:
        del dict[arr[l]]

    # 오른쪽 초밥 추가
    if arr[r] not in dict:
        dict[arr[r]] = 1 
    else:
        dict[arr[r]] += 1
    
    cnt = len(dict)
    maxValue = max(cnt, maxValue)

    l += 1
    r += 1    

print(maxValue)

#★=> 슬라이딩 윈도우를 활용하여 O(N)내에 해결가능하다.