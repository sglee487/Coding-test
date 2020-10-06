def solution(money):
    global result, dp
    dp = [[0 for _ in range(len(money))] for _ in range(3)]
    dp[0][0], dp[1][1], dp[2][2] = money[0], money[1], money[2]

    for i in range(2, len(money)):

        if i < len(money)-1:
            dp[0][i] = max(dp[0][i], dp[0][i - 2] + money[i])
            if i >= 3:
                dp[0][i] = max(dp[0][i], dp[0][i - 3] + money[i])

        if i >= 3:
            dp[1][i] = max(dp[1][i],dp[1][i-2]+money[i])
            dp[1][i] = max(dp[1][i], dp[1][i - 3] + money[i])

        if i >= 4:
            dp[2][i] = max(dp[2][i],dp[2][i-2]+money[i])
            dp[2][i] = max(dp[2][i], dp[2][i - 3] + money[i])

    # print(dp)
    return max(max(dp[0]),max(dp[1]),max(dp[2]))

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