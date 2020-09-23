def solution(n, lost, reserve):
    ls,rs = set(lost), set(reserve)
    ls, rs = ls - rs, rs - ls
    for l in ls.copy():
        if l-1 in rs:
            rs.remove(l-1)
            ls.remove(l)
        elif l+1 in rs:
            rs.remove(l+1)
            ls.remove(l)

    return n - len(ls)

print(solution(5,[2, 4],[1, 3, 5]),5)
print(solution(5,[2, 4],[3]),4)
print(solution(3,[3],[1]),2)