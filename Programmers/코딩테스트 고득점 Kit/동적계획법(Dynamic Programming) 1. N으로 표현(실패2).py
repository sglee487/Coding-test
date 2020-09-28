def solution(N, number):
    if N == number: return 1
    apns = set()
    apns.add(N)
    nl = [[],[N],[],[],[],[],[],[],[]]
    for i in range(1,8):
        for e in nl[i]:
            for j in range(1,i+1):
                if i+j>8:break
                for f in nl[j]:
                    if int(str(f) + str(e)) not in apns and not int(str(f) + str(e)) > 32000:
                        nl[i+j].append(int(str(f) + str(e)))
                        apns.add((int(str(f) + str(e))))
                        if int(str(f) + str(e)) == number: return i+j
                    if int(str(e) + str(f)) not in apns and not int(str(e) + str(f)) > 32000:
                        nl[i+j].append(int(str(e) + str(f)))
                        apns.add(int(str(e) + str(f)))
                        if int(str(e) + str(f)) == number: return i+j
                    if e+f not in apns and not e+f > 32000:
                        nl[i+j].append(e+f)
                        apns.add(e+f)
                        if int(e+f) == number: return i+j
                    if e-f not in apns and not e-f < 1:
                        nl[i+j].append(e-f)
                        apns.add(e-f)
                        if int(e-f) == number: return i+j
                    if e*f not in apns and not e*f>32000:
                        nl[i + j].append(e * f)
                        apns.add(e * f)
                        if e*f == number: return i+j
                    if e // f not in apns and e // f > 0:
                        nl[i + j].append(e // f)
                        apns.add(e // f)
                        if e // f == number: return i+j
                    if f // e not in apns and f // e > 0:
                        nl[i + j].append(f // e)
                        apns.add(f // e)
                        if f // e == number: return i+j

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
print(solution(5,20),4)
print(solution(5,30),3)

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