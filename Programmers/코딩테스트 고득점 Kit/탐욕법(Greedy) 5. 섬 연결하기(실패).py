def solution(n, costs):
    N = n

    graph = [[999999] * N for _ in range(N)]
    for a, b, c in costs:
        graph[a][b] = c
        graph[b][a] = c
    print(*graph,sep='\n')
    answer = 0
    for n in range(1, N):
        answer += min(graph[n][:n])

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]),4)
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]),9)