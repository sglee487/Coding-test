N = 12

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def move(log):
    if len(log) == N+1:
        return 1
    cnt = 0
    for i in range(4):
        nx, ny = log[-1][0] + dx[i], log[-1][1] + dy[i]
        if (nx, ny) not in log:
            cnt += move(log + [(nx,ny)])
    return cnt

print(move([(0,0)]))