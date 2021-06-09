import sys
sys.setrecursionlimit(10 ** 9)

sys.stdin = open("21608-상어 초등학교-1.txt", "r")

# input = sys.stdin.readline

N = int(input())
N2 = N**2

seq = []

studentl = [[] for _ in range(N2+1)]
for _ in range(N2):
    s, l1, l2, l3, l4 = map(int, input().split())
    studentl[s].append(l1)
    studentl[s].append(l2)
    studentl[s].append(l3)
    studentl[s].append(l4)
    seq.append(s)

# print(seq)

matrix = [[0]*(N) for _ in range(N)]

def searchmatrix(nows, studentl, matrix):
    cand = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0: continue
            nowlikecount, nowemptycount = searchcount(nows, r,c, studentl, matrix)
            cand.append((nowlikecount, nowemptycount, (r,c)))
    return cand

def searchcount(nows, r,c,studentl,matrix):
    likecount = 0
    emptycount = 0
    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not(0 <= nr < N and 0 <= nc < N): continue
        if matrix[nr][nc] in studentl[nows]:
            likecount += 1
        if matrix[nr][nc] == 0:
            emptycount += 1
            
    return likecount, emptycount

def likecount(nows, studentl, matrix):
    count = 0

    # 위 오 아래 왼
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if not(0 <= nr < N and 0 <= nc < N): continue
        if matrix[nr][nc] in studentl[nows]:
            count += 1
    return count


for nows in seq:
    cand = searchmatrix(nows, studentl, matrix)
    cand.sort(key=lambda x:(-x[0],-x[1],x[2]))
    dr, dc = cand[0][2][0], cand[0][2][1]
    # print(cand)
    # print(dr,dc)
    matrix[dr][dc] = nows

# print(*matrix, sep='\n')

result = 0

for r in range(N):
    for c in range(N):
        count = likecount(matrix[r][c], studentl, matrix)
        # print(count)
        if count > 0:
            result += 10 ** (count - 1)

print(result)