# ★ set 이용한 방법
# set키워드 괄호안에 리스트를 입력하여 만들거나, 문자열을 입력하여 직접 만들수도 있다.


import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    cnt = 0

    textList = set([input() for _ in range(N)])

    for _ in range(M):
        subString = input()
        if subString in textList:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()