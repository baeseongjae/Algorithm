T = int(input())

def solution(tc):
    data = input()
    arr = list(data)
    stack = []
    answer = 0

    for i in range(len(arr)-1, -1, -1):
        stack.append(arr[i])

    word = ''.join(stack)

    if word == data:
        answer = 1

    print(f"#{tc} {answer}")


for i in range(1, T+1):
    solution(i)

# 팰린드롬이면 1출력 아니면 0출력.