def solution(gems):
    N = len(gems)
    jemsorts = set(gems)
    SN = len(jemsorts)
    result = []
    minlength = len(gems)
    lp, rp = 0, SN
    while lp <= N - SN:
        if set(gems[lp:rp]) == jemsorts:
            if rp-lp < minlength:
                minlength = rp-lp
                result = []
            result.append([lp+1,rp])
            lp += 1
        else:
            if rp == N:
                lp += 1
            else:
                rp += 1
    result.sort()
    return result[0]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]),[3, 7])