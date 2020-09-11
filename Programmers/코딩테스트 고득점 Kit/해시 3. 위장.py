def solution(clothes):
    clodic = dict()
    for t, w in clothes:
        if not w in clodic:
            clodic[w] = 2
        else:
            clodic[w] += 1

    answer = 1
    for v in clodic.values():
        answer *= v
    return answer - 1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))