# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

def nts(x):
    s = "{0:b}".format(x)
    rs = ''
    for c in s:
        if c == '1':
            rs += '#'
        else:
            rs += ' '
    return rs

def solution(n, arr1, arr2):
    bok = [0] * n
    for i in range(n):
        bok[i] = arr1[i] | arr2[i]
    bok = list(map(nts,bok))

    return bok

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]),["#####","# # #", "### #", "# ##", "#####"])
print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]),["######", "### #", "## ##", " #### ", " #####", "### # "])