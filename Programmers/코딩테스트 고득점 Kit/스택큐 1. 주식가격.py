def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        count = 1
        for j in range(i+1, len(prices)):
            answer[i] = count
            if prices[i] <= prices[j]:
                count += 1
            else:
                break

    return answer

print(solution([1, 2, 3, 2, 3]))