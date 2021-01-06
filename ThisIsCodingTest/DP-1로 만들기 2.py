def solution(n):
    if n == 1: return 0
    tries = 0
    dp = [n]
    while True:
        dpafter = []
        for num in dp:
            if num % 5 == 0:
                dpafter.append(num//5)
            if num % 3 == 0:
                dpafter.append(num//3)
            if num % 2 == 0:
                dpafter.append(num//2)
            dpafter.append(num - 1)
        tries += 1
        if 1 in dpafter:
            break
        else:
            dp = dpafter[:]

    return tries

print(solution(26),3)