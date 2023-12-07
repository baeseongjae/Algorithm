# 문제를 바로 이해하지 못했음
import sys
input = sys.stdin.readline

n = int(input())
stack = []
curNum = 1
result = []

def solution(n):
    global stack, curNum, result
    for _ in range(n):
        inputNum = int(input())

        while inputNum >= curNum:
            stack.append(curNum)
            curNum += 1
            result.append('+')

        # input으로 들어온 수열값이 curNum보다 작을때
        # 이미 스택에 있으니 append할 필요가 없이 확인 로직만 짜면 됨.
        if stack[-1] == inputNum:
            stack.pop()
            result.append('-')
        else: # 스택 맨위의 숫자가 inputNum랑 다른수라면 주어진 수열은 만들지 못하는 수열이다.
            print("NO")
            return
    for i in result:
      print(i)

solution(n)