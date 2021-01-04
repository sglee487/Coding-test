a = b = 1
count = 0
while count < 11:
    c = a + b
    # 1자리씩으로 분할하여 각 자리의 합을 취득
    sum = 0
    for e in str(c):
        sum += int(e)
    if c % sum == 0:
        # 나누어 떨어지면 출력
        print(c)
        count += 1
    a, b = b, c