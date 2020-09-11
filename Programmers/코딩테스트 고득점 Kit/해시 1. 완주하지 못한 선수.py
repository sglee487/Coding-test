def solution(participant, completion):
    pardic = dict()
    comdic = dict()
    for p in participant:
        if not p in pardic:
            pardic[p] = 1
        else:
            pardic[p] += 1

    for c in completion:
        if pardic[c] == 1:
            del pardic[c]
        else:
            pardic[c] -= 1

    return list(pardic.keys())[0]

print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))