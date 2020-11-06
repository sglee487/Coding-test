def commonlongLCS(A,B):
    # A와 B의 공통 부분 문자열 중 가장 길이가 긴 문자열의 길이
    A = [0] + list(A)
    B = [0] + list(B)
    N = len(A)
    M = len(B)
    dp = [[999999] * (M) for _ in range(N)]

    for i in range(N):
        dp[i][0] = 0
    for i in range(M):
        dp[0][i] = 0

    for r in range(1,N):
        for c in range(1,M):
            if A[r] == B[c]:
                dp[r][c] = dp[r-1][c-1] + 1
            else:
                dp[r][c] = max(dp[r-1][c],dp[r][c-1])

    print(*dp,sep='\n')

    return


commonlongLCS('aabcab','bcabac')
commonlongLCS('apple','elppa')
commonlongLCS('abacabacab','cbadabcabac')


# https://github.com/ndb796/python-for-coding-test/blob/master/16/6.py
# 삽입
# 삭제
# 교체
# 최소 편집 거리(Edit Distance) 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 세 가지 경우 중에서 최솟값 찾기
            else:  # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]


# 최소 편집 거리 출력
print(edit_dist('cat', 'cut'))
print(edit_dist('sunday','saturday'))