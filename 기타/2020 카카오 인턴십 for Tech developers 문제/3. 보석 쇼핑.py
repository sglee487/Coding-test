def solution(gems):
    gem_len = len(set(gems))
    # print(set(gems))
    cur_have = dict()
    si, ei = 0, 0
    result = []

    while si < len(gems) and ei <= len(gems):
        if len(cur_have) < gem_len:
            if ei == len(gems): break
            if gems[ei] not in cur_have:
                cur_have[gems[ei]] = 1
            else:
                cur_have[gems[ei]] = cur_have[gems[ei]] + 1
            ei += 1
        else:
            result.append((si+1,ei,ei-si))
            # print(result)
            if cur_have[gems[si]] == 1:
                del cur_have[gems[si]]
            else:
                cur_have[gems[si]] = cur_have[gems[si]] - 1
            si += 1

    result = sorted(result, key=lambda x:(x[2],x[0]))
    # print(result)

    return [result[0][0],result[0][1]]