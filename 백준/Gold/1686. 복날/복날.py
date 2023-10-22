import math
from collections import deque

v, m = map(float, input().split())
xs, ys = map(float, input().split())
xt, yt = map(float, input().split())
bunker = []
cnt = 0 
maxRange = v * m * 60
result = False
visited = []

# 벙커 개수 안알려주는듯?
# EOF Error 잡기
while True:
    try:
        data = input()
        if not data:
            break
        x, y = map(float, data.split())
        bunker.append((x, y))    
    except:
        break
    

def calculateDist(a, b, x, y):
    return math.sqrt((x-a)**2 + (y-b)**2)

def BFS(xs, ys):
    global cnt, result
    queue = deque([(xs, ys, cnt)])
  
    while queue:
        curX, curY, cnt = queue.popleft()

        if calculateDist(curX, curY, xt, yt) < maxRange:
            result = True
            return result

        for item in bunker:
            xm, ym = item
            if item not in visited and calculateDist(curX, curY, xm, ym) < maxRange:
                queue.append((xm, ym, cnt+1))
                visited.append(item)

    return result

if BFS(xs, ys):
    print(f"Yes, visiting {cnt} other holes.")
else:
    print('No.')