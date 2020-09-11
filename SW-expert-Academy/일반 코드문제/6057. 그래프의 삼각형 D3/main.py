import sys

sys.stdin = open("s_input.txt", "r")

def dfs(si,j,rank):
    global tri_count
    if rank == 3:
        if si == j: tri_count += 1
        return
    for i in range(1, N+1):
        if ways[j][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(si, i, rank+1)
            visited[i] = False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # https://dheldh77.tistory.com/entry/SWEA-6057-%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%98-%EC%82%BC%EA%B0%81%ED%98%95
    N, M = map(int, input().split())
    ways = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        ways[a][b], ways[b][a] = 1, 1

    tri_count = 0
    visited = [False] * (N + 1)

    for i in range(1, N+1):
        for j in range(1, N+1):
            if j < i: visited[j] = True
            else: visited[j] = False
        for j in range(1, N+1):
            if not visited[j] and ways[i][j] == 1:
                visited[j] = True
                dfs(i,j,1)

    print("#{}".format(test_case),tri_count)
    # ///////////////////////////////////////////////////////////////////////////////////
