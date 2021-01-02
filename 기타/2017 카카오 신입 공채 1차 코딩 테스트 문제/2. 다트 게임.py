# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
import re

def solution(dartResult):
    scorere = re.findall(r"([\d]+[SDT][*#]?)",dartResult)
    print(scorere)
    scorel = [0] * 3
    for i, s in enumerate(scorere):
        scorel[i] = int(re.search("[\d]+",s).group())
        bonus = re.search("[SDT]",s).group()
        if bonus == 'S':
            scorel[i] = scorel[i] ** 1
        elif bonus == 'D':
            scorel[i] = scorel[i] ** 2
        elif bonus == 'T':
            scorel[i] = scorel[i] ** 3
        if re.search("[#*]",s):
            print(s)
            option = re.search("[#*]",s).group()
            if option == '*':
                scorel[i] = scorel[i] * 2
                if i > 0:
                    scorel[i-1] = scorel[i-1] * 2
            elif option == '#':
                scorel[i] = -scorel[i]

    print(scorel)
    return sum(scorel)

print(solution('1S2D*3T'),37)
print(solution('1D2S#10S'),9)
print(solution('1D2S0T'),3)
print(solution('1S*2T*3S'),23)
print(solution('1D#2S*3S'),5)
print(solution('1T2D3D#'),-4)
print(solution('1D2S3T*'),59)