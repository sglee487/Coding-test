# https://wikidocs.net/4309

# https://velog.io/@tjdud0123/%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%AC%B8%EC%A0%9C
# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/08/04/regex-usage-05-intermediate/
# https://www.delftstack.com/ko/howto/python/how-to-remove-whitespace-in-a-string/
# https://nachwon.github.io/regular-expressions/

from itertools import permutations
import re

def solution(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    cand = []

    for op_cand in prior:
        print(op_cand)
        temp2 = re.findall("\D",expression)
        print(temp2)
        temp2 = re.compile("\D").split('' + expression)
        print(temp2)
        temp = re.findall("(\D)",expression)
        print(temp)
        temp = re.compile("(\D)").split('' + expression)
        print(temp)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        cand.append(abs(int(temp[0])))
    return max(cand)