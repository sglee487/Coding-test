# 입력 사이에 공간이 있을때
list(map(int,input().split()))

# 입력 사이에 공간이 없을때
list(input())
board = [input() for _ in range(N)]

# 행렬 만들기
visited = [[0] * N for _ in range(N)]

# 정렬 기준 방법
room_numbers = sorted(room_numbers, key=lambda x: -x[1])

# 행렬 뒤집기
N, M = map(int, input().split())
HR = [0 for _ in range(N)]
for i, c in enumerate(zip(*H)):
    HR[i] = list(c)

# 행렬 방향
# 왼쪽, 아래, 오른쪽, 위
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
for i in range(4):
    new_y = start_y + dy[i]
    new_x = start_x + dx[i]
    if isSafe(new_y, new_x) and (new_y, new_x) not in stack:
        DFS(new_y, new_x)
# 아래, 우측아래, 우측, 우측위, 위, 좌측위, 좌측, 좌측아래
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
for d in range(8):
    y = r + dy[d]
    x = c + dx[d]
    if 0 <= x < N and 0 <= y < N:
        if board[y][x] == 0:
            click_zero(y, x)
        board[y][x] = 'C'
for d in range(8):
    x,y = r_q,c_q
    while 1<=x and x<=n and 1<=y and y<=n:
        ans += 1
        x+=dx[d]
        y+=dy[d]
        if (x,y) in block:
            break
    return (ans-8)