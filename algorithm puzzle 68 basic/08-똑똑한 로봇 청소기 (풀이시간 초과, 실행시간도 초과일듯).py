import copy
from collections import deque

Q = deque()
# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

Q.append((0,0,0,[(0,0)]))
result = 0
while Q:
    x, y, move, bodys = Q.pop()
    if move == 12:
        result += 1
        continue
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) not in bodys and move<12: 
            Q.append((nx,ny,move+1,copy.deepcopy(bodys+[(nx,ny)])))

print(result)