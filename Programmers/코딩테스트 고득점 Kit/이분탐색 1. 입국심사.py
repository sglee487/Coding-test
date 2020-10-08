def solution(n, times):
    start, end = 0, max(times) * n
    while start <= end:
        mid = (end + start) // 2
        if sum(map(lambda x:mid//x, times)) >= n:
            end = mid - 1
        else:
            start = mid + 1
    # print(start,end)
    return end+1

print(solution(6,[7, 10]),28)
print(solution(5,[10]),50)
print(solution(5,[1,2]),4)