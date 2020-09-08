def solution(gems):
    gem_len = len(set(gems))
    # print(set(gems))
    answer = []
    cur_have = []
    si, ei = 0, 0
    result = []

    while si < len(gems) and ei <= len(gems):
        if len(set(cur_have)) < gem_len:
            if ei == len(gems): break
            cur_have.append(gems[ei])
            ei += 1
        else:
            result.append((si+1,ei,ei-si))
            # print(result)
            cur_have.remove(gems[si])
            si += 1

    result = sorted(result, key=lambda x:(x[2],x[0]))
    # print(result)

    return [result[0][0],result[0][1]]