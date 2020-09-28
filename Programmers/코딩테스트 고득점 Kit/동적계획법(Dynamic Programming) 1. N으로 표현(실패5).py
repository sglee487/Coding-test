from collections import defaultdict

def solution(N, number):
    if N == number: return 1
    alnd = defaultdict(int)
    alnd[N] = 1
    nl = [[],[N],[],[],[],[],[],[],[]]
    result = 9
    for i in range(1,8):
        for e in nl[i]:
            for j in range(1,i+1):
                if i+j>8:break
                for f in nl[j]:
                    if not int(str(f) + str(e)) > 32000 and (
                            int(str(f) + str(e)) not in alnd or alnd[int(str(f) + str(e))] > i+j):
                        nl[i+j].append(int(str(f) + str(e)))
                        if int(str(f) + str(e)) in alnd:
                            nl[alnd[int(str(f) + str(e))]].remove(int(str(f) + str(e)))
                        alnd[int(str(f) + str(e))] = i+j
                        if int(str(f) + str(e)) == number:
                            if i+j < result: result = i+j
                    if not int(str(e) + str(f)) > 32000 and (
                            int(str(e) + str(f)) not in alnd or alnd[int(str(e) + str(f))] > i+j):
                        nl[i+j].append(int(str(e) + str(f)))
                        if int(str(e) + str(f)) in alnd:
                            nl[alnd[int(str(e) + str(f))]].remove(int(str(e) + str(f)))
                        alnd[int(str(e) + str(f))] = i + j
                        if int(str(e) + str(f)) == number:
                            if i + j < result: result = i + j
                    if not e+f > 32000 and (
                            e+f not in alnd or alnd[e+f] > i+j):
                        nl[i+j].append(e+f)
                        if e+f in alnd:
                            nl[alnd[e+f]].remove(e+f)
                        alnd[e+f] = i + j
                        if int(e+f) == number:
                            if i+j < result: result = i+j
                    if not e-f < 1 and (
                            e-f not in alnd or alnd[e-f] > i+j):
                        nl[i+j].append(e-f)
                        if e-f in alnd:
                            nl[alnd[e-f]].remove(e-f)
                        alnd[e-f] = i + j
                        if int(e-f) == number:
                            if i + j < result: result = i + j
                    if not f-e < 1 and (
                            f-e not in alnd or alnd[f-e] > i+j):
                        nl[i+j].append(f-e)
                        if f-e in alnd:
                            nl[alnd[f-e]].remove(f-e)
                        alnd[f-e] = i + j
                        if int(f-e) == number:
                            if i + j < result: result = i + j
                    if not e*f>32000 and (
                            e*f not in alnd or alnd[e*f] > i+j):
                        nl[i + j].append(e * f)
                        if e*f in alnd:
                            nl[alnd[e*f]].remove(e*f)
                        alnd[e*f] = i + j
                        if e*f == number:
                            if i + j < result: result = i + j
                    if e // f > 0 and (
                            e//f not in alnd or alnd[e//f] > i+j):
                        nl[i + j].append(e // f)
                        if e//f in alnd:
                            nl[alnd[e//f]].remove(e//f)
                        alnd[e//f] = i + j
                        if e // f == number:
                            if i + j < result: result = i + j
                    if f // e > 0 and (
                            f//e not in alnd or alnd[f//e] > i+j):
                        nl[i + j].append(f // e)
                        if f//e in alnd:
                            nl[alnd[f//e]].remove(f//e)
                        alnd[f//e] = i + j
                        if f // e == number:
                            if i + j < result: result = i + j
        # if result < 9:
        #     return result
    # print(*nl,sep='\n')
    print(alnd)
    for i,l in enumerate(nl):
        for e in l:
            if e == number: return i
    return -1

print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121),5)
print(solution(5,1010),4)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)

'''
5의 경우 할수있는거
1개
5
2개
55, 5+5=10, 5-5=0, 5*5=25, 5/5=1
3개
(55)5, 5(55), 55+5=60, 5+55=60, 55-5=50, -5+55=50, 55*5=275, 5*55=275, 55/5=11, 5/55=0
(10)5, 5(10), 10+5=15, 5+10=15, 10-5=5, -5+10=5, 10*5=50, 5*10=50, 10/5=2, 5/10=0
(0)5, 5(0), 0+5=5, 5+0=5, 0-5=-5, -5+0=-5, 0*5=0, 5*0=0, 0//5=0, 5//0=error
(25)5, 5(25), 25+5=30, 5+25=30, 25-5=20, -5+25=20, 25*5=125, 5*25=125, 25/5=5, 5/25=0
(1)5, 5(1), 1+5=6, 5+1=6, 1-5=-4, -5+1=-4, 1*5=5, 5*1=5, 1/5=0, 5/1=5
'''