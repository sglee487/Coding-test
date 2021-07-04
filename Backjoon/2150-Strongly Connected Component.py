import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2150-Strongly Connected Component-2.txt", "r")

# input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

pa = [0] * (V+1)
stack = []
SSC = []
finished = [False] * (V+1)
id = 1

def dfs(n):
    global id
    pa[n] = id
    id += 1
    stack.append(n)

    parent = pa[n]
    for child in graph[n]:
        if not pa[child]:
            parent = min(parent, dfs(child))
        elif not finished[child]:
            parent = min(parent, pa[child])

    if parent == pa[n]:
        ssc = []
        while True:
            last = stack.pop()
            ssc.append(last)
            finished[last] = True
            if last == n:
                break
        SSC.append(sorted(ssc))

    return parent


for v in range(1, V+1):
    if not pa[v]:
        dfs(v)

print(len(SSC))
SSC.sort(key=lambda x:x[0])
for ssc in SSC:
    print(*sorted(ssc), end=' ')
    print(-1)