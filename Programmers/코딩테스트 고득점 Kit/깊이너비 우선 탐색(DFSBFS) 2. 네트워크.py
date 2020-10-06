def Make_Set(x):
    p[x] = x # 자기 자신
    rank[x] = 0

def Find_Set(x):
    if x != p[x]: # x가 루트가 아닌 경우
        p[x] = Find_Set(p[x]) # Path Compression
    return p[x]

def Union(x,y):
    Link(Find_Set(x), Find_Set(y))

def Link(x,y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1

def solution(n, computers):
    global p, rank
    N = n

    p = [0] * N
    rank = [0] * N
    for i in range(N):
        Make_Set(i)

    result = 0
    for i in range(N):
        for j in range(i+1,N):
            if computers[i][j] == 1: Union(i,j)
    for i,e in enumerate(p):
        if i == e: result += 1
    return result

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]),2)
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]),1)