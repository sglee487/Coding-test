def solution(money):
    # global result, dp
    # dp = [[0 for _ in range(len(money))] for _ in range(3)]
    # dp[0][0], dp[1][1], dp[2][2] = money[0], money[1], money[2]
    dp = [0] * len(money)
    dp[0] = money[0]
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i],dp[i-2]+money[i])
        if i >= 3:
            dp[i] = max(dp[i], dp[i - 3] + money[i])
    result1 = max(dp)

    dp = [0] * len(money)
    dp[1] = money[1]
    dp[2] = money[2]
    for i in range(3, len(money)):
        dp[i] = max(dp[i],dp[i-2]+money[i])
        dp[i] = max(dp[i], dp[i - 3] + money[i])
    result2 = max(dp)

    # dp = [0] * len(money)
    # dp[2] = money[2]
    # for i in range(4, len(money)):
    #     dp[i] = max(dp[i],dp[i-2]+money[i])
    #     dp[i] = max(dp[i], dp[i - 3] + money[i])
    # result3 = max(dp)
    return max(result1,result2)

print(solution([1, 2, 3, 1]),4)
print(solution([6, 7, 6, 4]),12)
print(solution([1,9,3,5,7,1,5]),21)
print(solution([1, 2, 3]),3)
print(solution([1, 2, 3, 1]),4)
print(solution([1, 2, 3, 1, 2]),5)
print(solution([1, 2, 3, 1, 2, 3]),6)
print(solution([1, 2, 3, 1, 2, 3, 4]),9)
print(solution([1,1,1]),1)
print(solution([1,1,1,1]),2)
print(solution([1,1,1,1,1]),2)
print(solution([1,1,1,1,1,1]),3)
print(solution([1,1,1,1,1,1,1]),3)
print(solution([1,1,1,1,1,1,1,1]),4)
print(solution([1,1,1,1,1,1,1,1,1]),4)
print(solution([1,1,1,1,1,1,1,1,1,1]),5)