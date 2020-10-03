def solution(m, n, puddles):
    board = [[0]*(m+1) for _ in range(n+1)]

    for r in range(1,n+1):
        for c in range(1,m+1):
            if r == 1 and c == 1:
                board[r][c] = 1
                continue
            if [c,r] in puddles: continue
            board[r][c] = board[r-1][c] + board[r][c-1]

    print(*board, sep='\n')
    return board[n][m] % 1000000007

print(solution(4,3,[[2, 2]]),4)
print(solution(4,3,[[3, 2]]),4)
print(solution(4,3,[[4, 2]]),4)
print(solution(4,3,[[2,2],[3, 2]]),4)
print(solution(4,3,[[2,2],[4, 2]]),4)
print(solution(4,3,[[2,2],[3,2],[4, 2]]),4)