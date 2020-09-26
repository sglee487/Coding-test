def solution(routes):
    et = {}
    te = []
    for s,e in routes:
        te.append((s,'in'))
        te.append((e,'out'))
        et[s] = e
    te.sort()
    answer = 0
    outstack = []
    for t,w in te:
        if w == 'in':
            outstack.append(et[t])
        if w == 'out' and t in outstack:
            outstack.clear()
            answer += 1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]),2)
print(solution([[-20,-10], [10,20]]),2)
print(solution([[-20,-10], [-15,20]]),1)