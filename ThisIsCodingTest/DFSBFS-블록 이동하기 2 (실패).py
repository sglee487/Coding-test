# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

def solution(board):
    N = len(board)
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    v = [[0] * N for _ in range(N)]
    Q = deque([(0,0,0,1,0,0)])
    v[0][0], v[0][1] = 1, 1
    result = 0
    print(*board,sep='\n')
    while Q:
        leftupr, leftupc, rightdownr, rightdownc, gase, step = Q.popleft()
        if (leftupr,leftupc) == (N-1,N-1) or (rightdownr,rightdownc) == (N-1,N-1):
            result = step
            break
        # 4방향 이동
        for i in range(4):
            nlur, nluc = dy[i] + leftupr, dx[i] + leftupc
            nrdr, nrdc = dy[i] + rightdownr, dx[i] + rightdownc
            if (0<=nlur<N and 0<=nluc<N and 0<=nrdr<N and 0<=nrdc<N) \
                and (board[nlur][nluc] == 0 and board[nrdr][nrdc] == 0) \
                and (v[nlur][nluc] == 0 or v[nrdr][nrdc] == 0):
                v[nlur][nluc],v[nrdr][nrdc] = 1, 1
                Q.append((nlur,nluc,nrdr,nrdc, gase, step+1))

        # 가로
        if gase == 0:
            if (leftupr-1>=0 and board[rightdownr-1][rightdownc] == 0 and board[leftupr-1][leftupc-1] == 0) \
                and v[leftupr-1][rightdownc-1] == 0:
                v[leftupr - 1][rightdownc - 1] = 1
                Q.append((leftupr-1,leftupc,rightdownr,leftupc, 1, step+1))
            if (leftupr-1>=0 and board[leftupr-1][leftupc] == 0 and board[rightdownr-1][rightdownc] == 0) \
                and v[rightdownr-1][rightdownc] == 0:
                v[rightdownr - 1][rightdownc] = 1
                Q.append((rightdownr-1,rightdownc,rightdownr,rightdownc, 1, step+1))
            if (leftupr+1<N and board[rightdownr+1][rightdownc] == 0 and board[leftupr+1][leftupc] == 0) \
                and v[leftupr+1][leftupc] == 0:
                v[leftupr + 1][leftupc] = 1
                Q.append((leftupr,leftupc,leftupr+1,leftupc, 1, step+1))
            if (leftupr+1<N and board[leftupr+1][leftupc] == 0 and board[rightdownr+1][rightdownc] == 0) \
                and v[rightdownr+1][rightdownc] == 0:
                v[rightdownr + 1][rightdownc] = 1
                Q.append((rightdownr,rightdownc,rightdownr+1,rightdownc, 1, step+1))
        #세로
        elif gase == 1:
            if (leftupc - 1 >= 0 and board[rightdownr][rightdownc-1] == 0 and board[leftupr][leftupc - 1] == 0) \
                    and v[leftupr][leftupc - 1] == 0:
                v[leftupr][leftupc - 1] = 1
                Q.append((leftupr, leftupc-1, leftupr, rightdownc, 0, step + 1))
            if (leftupc + 1 < N and board[rightdownr][rightdownc+1] == 0 and board[leftupr][leftupc + 1] == 0) \
                    and v[leftupr][leftupc + 1] == 0:
                v[leftupr][leftupc + 1] = 1
                Q.append((leftupr, leftupc, leftupr, rightdownc+1, 0, step + 1))
            if (leftupc - 1 >= 0 and board[leftupr][leftupc-1] == 0 and board[rightdownr][rightdownc-1] == 0) \
                    and v[rightdownr][rightdownc-1] == 0:
                v[rightdownr][rightdownc-1] = 1
                Q.append((leftupr-1, rightdownc-1, rightdownr, rightdownc, 0, step + 1))
            if (leftupc + 1 < N and board[leftupr][leftupc+1] == 0 and board[rightdownr][rightdownc + 1] == 0) \
                    and v[rightdownr][rightdownc + 1] == 0:
                v[rightdownr][rightdownc + 1] = 1
                Q.append((rightdownr, rightdownc, rightdownr, rightdownc+1, 0, step + 1))
        print(Q)
    return result

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]),7)
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]),21)
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]),11)
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]),33)