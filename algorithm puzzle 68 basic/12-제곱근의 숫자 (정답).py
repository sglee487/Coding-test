from math import sqrt

# 정수 부분을 포함하는 경우
i = 1
while True:
    i += 1
    # 소수점을 제거하고 왼쪽 10문자 추출
    string = '{:10.10f}'.format(sqrt(i)).replace('.','')[0:10]
    # 중복을 제거해서 10문자라면 종료
    if len(set(string)) == 10:
        break

print(i)

# 소수 부분만 계산하는 경우
i = 1
while True:
    i += 1
    # 소수점으로 분할하여 소수 부분만을 취득
    string = '{:10.10f}'.format(sqrt(i)).split('.')[1]
    # 소수 부분의 중복을 제거하고 10문자라면 종료
    if len(set(string)) == 10:
        break

print(i)