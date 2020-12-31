answer = 0
for num in range(2,10001,2):
    next_num = num * 3 + 1
    while True:
        if next_num == num:
            answer += 1
            break
        elif next_num == 1:
            break
        else:
            if next_num % 2 == 0:
                next_num = next_num // 2
            else:
                next_num = next_num * 3 + 1
print(answer)