
import sys

sys.stdin = open("sample_input.txt", "r")

def way(v):

    Q.append(v)
    visited.append(v)

    while Q:
        v = Q.pop(0)
        for i in Edict[v]:
            w = i
            if w not in visited:
                Q.append(w)
                visited.append(w)
                ds[w] = ds[v] + 1
                if w == end:
                    return


    return


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    V, E = map(int, input().split())
    Edict = dict()

    for i in range(V):
        Edict[i + 1] = list()
    for _ in range(E):
        v, e = map(int, input().split())
        Edict[v].append(e)
        Edict[e].append(v)

    start, end = map(int, input().split())

    ds = [0] * (V+1)
    visited = []
    Q = []
    way(start)

    print("#{}".format(test_case),ds[end])


    # ///////////////////////////////////////////////////////////////////////////////////
