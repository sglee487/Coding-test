# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        man = arr1[i] | arr2[i]
        man = "{0:b}".format(man)
        man = '0' * (n - len(man)) + man
        man = man.replace('1', '#')
        man = man.replace('0', ' ')
        answer.append(man)

    return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]),["#####","# # #", "### #", "# ##", "#####"])
print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]),["######", "### #", "## ##", " #### ", " #####", "### # "])