def solution(n):
    tria = [[0] * n for _ in range(n)]

    i = 0
    j = 0

    count = 1
    loop = n
    while loop > 0:
        # print(loop)
        for _ in range(loop):
            tria[i][j] = count
            count += 1
            i += 1
            # print(*tria, sep='\n')
            # print()
        loop -= 1
        i -= 1
        j += 1
        # print(loop)
        for _ in range(loop):
            tria[i][j] = count
            count += 1
            j += 1
            # print(*tria, sep='\n')
            # print()

        loop -= 1
        i -= 1
        j -= 2
        # print(loop)
        for _ in range(loop):
            tria[i][j] = count
            count += 1
            i -= 1
            j -= 1
            # print(*tria, sep='\n')
            # print()
        loop -= 1
        i += 2
        j += 1

    # print(*tria, sep='\n')

    answer = []
    for row in tria:
        for c in row:
            if c != 0:
                answer.append(c)
            else:
                break

    return answer

print(solution(4))