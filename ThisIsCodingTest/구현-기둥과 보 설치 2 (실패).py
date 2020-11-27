# https://programmers.co.kr/learn/courses/30/lessons/60061

def isright(board,n):
    for r in range(n+1):
        for c in range(n+1):
            # 기둥
            if board[r][c] == 0:
                if (r == 0): continue
                if (c>=1 and board[r][c-1] == 1): continue
                if (c+1<=n and board[r][c+1] == 1): continue
                if r >= 1 and board[r-1][c] == 0: continue
                return False
            # 보
            elif board[r][c] == 1:
                if r >= 1 and board[r-1][c] == 0: continue
                if r >= 1 and c+1<=n and board[r-1][c+1] == 0: continue
                if (c-1>=0 and board[r][c-1] == 1) and (c+1<=n and board[r][c+1] == 1): continue
                return False
    return True

def solution(n, build_frame):
    board = [[-1] * (n+1) for _ in range(n+1)]
    for x, y, a, b in build_frame:
        # 구조물 삭제
        if b == 0:
            board[y][x] = -1
            if not (isright(board,n)):
                board[y][x] = a
        # 구조물 설치
        elif b == 1:
            board[y][x] = a
            if not(isright(board,n)):
                board[y][x] = -1
    print(*board,sep='\n')
    answer = []
    for r in range(n+1):
        for c in range(n+1):
            if board[r][c] == 0:
                answer.append([c,r,0])
            elif board[r][c] == 1:
                answer.append([c,r,1])
    answer.sort()
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]),[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]])
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]),[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]])