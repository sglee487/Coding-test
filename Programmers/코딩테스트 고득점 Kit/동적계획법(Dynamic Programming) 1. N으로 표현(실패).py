def solution(N, number):
    if N == number: return 1
    apns = set()
    apns.add(N)
    nl = [[],[N]]
    i=1
    while i <= 7:
        nl.append([])
        for e in nl[i]:
            if e < 1 or e > 32000: continue
            if e >= 0 and int(str(N) + str(e)) not in apns:
                nl[i+1].append(int(str(N) + str(e)))
                apns.add((int(str(N) + str(e))))
                if int(str(N) + str(e)) == number: return i+1
            if int(str(e) + str(N)) not in apns:
                nl[i+1].append(int(str(e) + str(N)))
                apns.add(int(str(e) + str(N)))
                if int(str(e) + str(N)) == number: return i+1
            if e+N not in apns:
                nl[i+1].append(e+N)
                apns.add(e+N)
                if int(e+N) == number: return i+1
            if e-N not in apns:
                nl[i+1].append(e-N)
                apns.add(e-N)
                if int(e-N) == number: return i+1
            if e*N not in apns:
                nl[i + 1].append(e * N)
                apns.add(e * N)
                if e*N == number: return i+1
            if e // N not in apns and e // N > 0:
                nl[i + 1].append(e // N)
                apns.add(e // N)
                if e // N == number: return i+1
            if e > 0 and N // e not in apns:
                nl[i + 1].append(N // e)
                apns.add(N // e)
                if N // e == number: return i+1
        i += 1

    return -1

print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121))
print(solution(5,1010),4)

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