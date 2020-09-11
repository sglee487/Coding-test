import sys

sys.stdin = open("sample_input.txt", "r")

def way(start_y,start_x,sum):
    global minsum

    Q.append((start_y,start_x,sum))
    visited.append((start_y,start_x))
    minmiro[start_y][start_x] = sum


    while Q:
        start_y, start_x,sum = Q.pop(0)
        for i in range(2):
            new_y = start_y + dy[i]
            new_x = start_x + dx[i]
            if new_y < N and new_x < N :
                if (sum + minmiro[start_y][start_x] < minmiro[new_y][new_x]):
                    minmiro[new_y][new_x] = sum + minmiro[start_y][start_x]
                    Q.append((new_y,new_x,minmiro[new_y][new_x]))


                # print(new_y,new_x,sum + miro[new_y][new_x])
                # if (new_y == N-1 and new_x == N-1) and (sum + miro[new_y][new_x] < minsum):
                #     minsum = sum + miro[new_y][new_x]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    miro = [list(map(int, input().split())) for _ in range(N)]
    minmiro = [[99999] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    dx = [1,0] # 오른쪽, 아래
    dy = [0,1] # 오른쪽, 아래

    minmiro[0][0] = miro[0][0]
    for i in range(1,N):
        minmiro[0][i] = minmiro[0][i-1] + miro[0][i]
    for i in range(1,N):
        minmiro[i][0] = minmiro[i-1][0] + miro[i][0]
    for r in range(1,N):
        for c in range(1,N):
            if (miro[r][c] + minmiro[r-1][c]) < (miro[r][c] + minmiro[r][c-1]):
                minmiro[r][c] = miro[r][c] + minmiro[r-1][c]
            else:
                minmiro[r][c] = miro[r][c] + minmiro[r][c-1]


    Q = []
    minsum = 999999

    print("#{}".format(test_case),minmiro[N-1][N-1])

    # ///////////////////////////////////////////////////////////////////////////////////
