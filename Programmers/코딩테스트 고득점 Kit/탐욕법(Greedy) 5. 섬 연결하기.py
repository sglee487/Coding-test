# 상호배타 집합 트리
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

def solution(n, costs):
    global p, rank
    N = n

    cs = sorted(costs,key=lambda x:x[2])
    print(cs)
    p = [0] * N
    rank = [0] * N
    for i in range(N):
        Make_Set(i)

    result = 0
    for a, b, c in cs:
        if Find_Set(a) != Find_Set(b):
            Union(a,b)
            result += c

    return result

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]),4)
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]),9)
print(solution(5,[[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]),8)