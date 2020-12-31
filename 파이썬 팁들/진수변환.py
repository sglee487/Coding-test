# https://velog.io/@ykwon3357/%ED%8C%8C%EC%9D%B4%EC%8D%AC-n%EC%A7%84%EC%88%98-%EB%B3%80%ED%99%98
# 10진수를 n진수로 변환
# 재귀함수 이용
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base) # n을 base로 나눈 몫과 나머지를 튜플형태로 반환
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

print (convert(233, 2))
print (convert(45, 3))
print (convert(233, 8))
print (convert(233, 16))

# 2진수로 8진수로 16진수로
num = 100
print(bin(num).replace("0b",""))
print(oct(num).replace("0o",""))
print(hex(num).replace("0x",""))

print("{0:b}".format(num))
print("{0:o}".format(num))
print("{0:d}".format(num)) # 10진수
print("{0:x}".format(num))

# https://programmers.co.kr/learn/courses/4008/lessons/12733
# n진수를 10진수로 변환
num = '3212'
base = 5
answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
print(answer)

num = '3212'
base = 5
answer = int(num, base)
print(answer)