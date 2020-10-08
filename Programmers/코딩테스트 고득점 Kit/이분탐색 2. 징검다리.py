def solution(distance, rocks, n):
    # 최소 거리 만들기로 돌을 제거.
    sre = [0] + sorted(rocks) + [distance]
    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2
        i, j = 0, 1
        err = 0
        while i < len(sre):
            while j < len(sre) and sre[i] + mid > sre[j]:
                j += 1
                err += 1
            i = j
            j = i+1
        if err > n:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(solution(25,[2, 11, 14, 17, 21],2),4)
print(solution(25,[2, 11, 14, 17, 21],5),25)
print(solution(25,[2, 11, 14, 17, 21],4),11)
print(solution(25,[2, 14, 11, 21, 17],2),4)
print(solution(25,[2, 14, 11, 21, 17],5),25)
print(solution(25,[2, 14, 11, 21, 17],4),11)