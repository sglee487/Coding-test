from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]),2)
print(solution(3,[[1,2], [2,3]]),3)
print(solution(3,[[1, 2], [1, 3]]),1)
print(solution(4,[[1,2], [2,3],[3,4]]),4)
print(solution(4,[[1,2], [1,3],[3,4]]),1)