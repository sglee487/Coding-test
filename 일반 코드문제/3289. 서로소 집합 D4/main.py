import sys

sys.stdin = open("sample_input.txt", "r")

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

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    p = [0] * (N+1)
    rank = [0] * (N+1)
    for i in range(1,N+1):
        Make_Set(i)

    result = []
    for _ in range(M):
        command, a, b = map(int, input().split())
        if command == 0:
            Union(a, b)
        if command == 1:
            if Find_Set(a) == Find_Set(b):
                result.append(1)
            else:
                result.append(0)

    print("#{}".format(test_case),end=' ')
    print(*result,sep='')
    # ///////////////////////////////////////////////////////////////////////////////////