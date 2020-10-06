def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)

print(solution([1, 2, 3, 1]),4)
print(solution([6, 7, 6, 4]),12)
print(solution([1,9,3,5,7,1,5]),21)
print(solution([1, 2, 3]),3)

def solution(money):
    answer = 0

    dp1 = [] # 첫 집을 털었을 때
    dp2 = [] # 첫 집을 안 털고 두 번째 집을 털었을 때
    dp3 = [] # 첫 집과 두 번째 집을 안 털었을 때
    for i in money:
        dp1.append(0)
        dp2.append(0)
        dp3.append(0)
    dp1[0] = money[0]
    dp1[1] = dp1[0]
    dp2[1] = money[1]

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        dp3[i] = max(dp3[i - 1], dp3[i - 2] + money[i])
    e = len(money) - 1
    dp1[e] = dp1[e - 1]
    dp2[e] = max(dp2[e - 1], dp2[e - 2] + money[e])
    dp3[e] = max(dp3[e - 1], dp3[e - 2] + money[e])
    answer = max(dp1[e], dp2[e], dp3[e])

    return answer

print(solution([1, 2, 3, 1]),4)
print(solution([6, 7, 6, 4]),12)
print(solution([1,9,3,5,7,1,5]),21)
print(solution([1, 2, 3]),3)