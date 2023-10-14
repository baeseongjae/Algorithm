from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
# 입력예제1 => a, c, i, s, t, w

vowels = set(('a', 'e', 'i', 'o', 'u'))
# 최소 자음2개 모음1개 구성.
def check(arr):
    vcnt, ccnt = 0, 0
    for item in arr:
        if item in vowels:
            vcnt += 1
        else:
            ccnt += 1

    if vcnt >= 1 and ccnt >= 2:
        return True
    else:
        return False
    
def DFS(tmp):
    if len(tmp) == L:
        # 체킹
        if check(tmp):
            print(''.join(tmp))
            return
    
    # a c i s t w
    for i in range(len(tmp), C):
        if tmp[-1] < arr[i]:
            tmp.append(arr[i])
            DFS(tmp)
            tmp.pop()


for i in range(C-L+1):
    tmp = [arr[i]]
    DFS(tmp)
