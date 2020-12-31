from itertools import combinations

sajik = ['+','_','*','//','','','']
answer = []
for num in range(1000,10000):
    for comb in combinations(sajik,3):
        if comb == ('','',''): continue
        try:
            numc = eval(str(num)[0] + comb[0] + str(num)[1] + comb[1] + str(num)[2] + comb[2] + str(num)[3])
        except:
            continue
        if str(num) == str(numc)[::-1]:
            answer.append(numc)

print(answer)
