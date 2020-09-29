def solution(triangle):
    sumtri = triangle[:]
    for i in range(1,len(sumtri)):
        for j in range(len(sumtri[i])):
            if j == 0: sumtri[i][j] += sumtri[i-1][j]
            elif j == len(sumtri[i])-1: sumtri[i][j] += sumtri[i-1][j-1]
            else:
                if sumtri[i][j] + sumtri[i-1][j] > sumtri[i][j] + sumtri[i-1][j-1]:
                    sumtri[i][j] += sumtri[i-1][j]
                else:
                    sumtri[i][j] += sumtri[i - 1][j-1]

    return max(sumtri[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]),30)