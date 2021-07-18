import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("9252-LCS 2-1.txt", "r")

input = sys.stdin.readline

def dfs(sr,sc):
    global M,N
    if sdp[sr][sc]:
        return sdp[sr][sc]
    rs = ''
    for r in range(sr+1, N):
        for c in range(sc+1, M):
            if sames[r][c] :
                ts = dfs(r, c)
                if len(rs) < len(ts):
                    rs = ts
    sdp[sr][sc] = sames[sr][sc] + rs

    return sdp[sr][sc]

A = input().strip()
B = input().strip()
N = len(A)
M = len(B)
sames = [[''] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            sames[i][j] = A[i]

print(*sames, sep='\n')
print()

ldp = [[0] * M for _ in range(N)]
sdp = [[''] * M for _ in range(N)]
answer = ''

for r in range(N):
    for c in range(M):
        if sames[r][c]:
            temp = dfs(r,c)
            if len(answer) < len(temp):
                answer = temp

# print(*ldp, sep='\n')
print(*sdp, sep='\n')
print(len(answer))
print(answer)