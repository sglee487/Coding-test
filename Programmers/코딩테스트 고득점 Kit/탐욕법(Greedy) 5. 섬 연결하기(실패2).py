def solution(n, costs):
    N = n

    cs = sorted(costs,key=lambda x:x[2])
    conset = set()
    print(cs)
    result = 0
    for a, b, c in cs:
        if a in conset and b in conset:
            continue
        result += c
        conset.add(a)
        conset.add(b)
        print(conset)
        if len(conset) == N: break

    return result

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]),4)
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]),9)
print(solution(5,[[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]),8)