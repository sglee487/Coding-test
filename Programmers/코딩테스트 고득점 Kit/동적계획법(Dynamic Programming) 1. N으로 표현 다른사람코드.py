def solution(N, number):
    if N == number: return 1
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)):
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1

print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121),7)
print(solution(5,1010),7)
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
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)

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