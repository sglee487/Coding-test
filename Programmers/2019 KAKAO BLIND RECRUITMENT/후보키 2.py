def notsub(nowbit, candidate_bits):
    for candibit in candidate_bits:
        if nowbit & candibit == candibit:
            return False
    return True


def solution(relation):
    rl = len(relation)
    cl = len(relation[0])

    result = 0
    candidate_bits = []
    for bit in range((1<<cl)):
        informset = set()
        for r in range(rl):
            cs = ''
            for c in range(cl):
                if bit & (1 << c):
                    cs += relation[r][c]
            informset.add(cs)
        if len(informset) == rl and notsub(bit,candidate_bits):
            candidate_bits.append(bit)
            result += 1
    return result

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]),2)