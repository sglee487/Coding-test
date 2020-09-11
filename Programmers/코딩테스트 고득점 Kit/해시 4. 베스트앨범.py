from collections import defaultdict

def solution(genres, plays):
    sd = defaultdict(int)
    giap = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres,plays)):
        sd[g] += p
        giap[g].append((i,p))

    gen_sorted = sorted(sd.items(),key=lambda x:-x[1])

    answer = []
    for g,_ in gen_sorted:
        sorted_g = sorted(giap[g],key=lambda x:-x[1])
        i = 0
        while i < 2 and i < len(sorted_g):
            answer.append(sorted_g[i][0])
            i += 1

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]))