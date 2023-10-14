N = int(input())
answer = 0
row = [0] * N

def nQueen(x):
    global answer
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            row[x] = i
            for j in range(x):
                if row[x] == row[j] or abs(row[x] - row[j]) == abs(x - j):
                    break
          
            else:
                nQueen(x+1)
      
nQueen(0)
print(answer)