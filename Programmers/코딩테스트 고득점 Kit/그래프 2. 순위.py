from collections import deque

def solution(n, results):
    parent = [[] for _ in range(n+1)]
    child = [[] for _ in range(n+1)]
    for p,c in results:
        parent[c].append(p)
        child[p].append(c)
    # print(parent)
    # print(child)
    result = 0
    Q = deque()
    for s in range(1,n+1):
        Q.append(s)
        visited = [False] * (n+1)
        loseset = set()
        while Q:
            w = Q.popleft()
            if visited[w]: continue
            visited[w] = True

            for p in parent[w]:
                if not visited[p]:
                    Q.append(p)
                    loseset.add(p)

        Q.append(s)
        visited = [False] * (n + 1)
        winset = set()
        while Q:
            w = Q.popleft()
            if visited[w]: continue
            visited[w] = True

            for c in child[w]:
                if not visited[c]:
                    Q.append(c)
                    winset.add(c)

        # print(s, winset, loseset)
        if len(winset) + len(loseset) == n-1: result += 1

    return result

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]),2)
print(solution(3,[[1,2], [2,3]]),3)
print(solution(3,[[1, 2], [1, 3]]),1)
print(solution(4,[[1,2], [2,3],[3,4]]),4)
print(solution(4,[[1,2], [1,3],[3,4]]),1)