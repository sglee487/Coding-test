import sys

sys.stdin = open("sample_input.txt", "r")

def printmatrix(matrix):
    for i in matrix:
        print(i)
# https://hongsj36.github.io/2020/02/02/Ad_GraphMST/
def Dijkstra_custom(tera):
    # 원래 visited 리스트 만들어서 append 했었는데 역시 실행시간에 문제가 발생.
    # 나도 고정배열 써야지
    visited = [[False]*N for _ in range(N)]
    # d = [[1000] * N for _ in range(N)]
    d = [[float('inf')] * N for _ in range(N)]
    # Q = []
    Q = set()
    d[0][0] = 0
    # Q.append((0,0))
    Q.add((0,0))
    while True:
        # 최소 거리부터 집합 S에 합치는 다익스트라 알고리즘임.
        y,x = 0,0
        # minfuel = 1000000
        minfuel = float('inf')
        for r, c in Q:
            if d[r][c] < minfuel and not visited[r][c]:
                minfuel = d[r][c]
                y,x = r,c

        visited[y][x] = True
        Q.remove((y,x))
        if y == N-1 and x == N-1:
            return d[N-1][N-1]
        for i in range(4):
            new_y, new_x = y + dy[i], x + dx[i]
            if 0<=new_y<N and 0<=new_x<N and not visited[new_y][new_x]:
                if tera[new_y][new_x] > tera[y][x]:
                    fuel = d[y][x] + tera[new_y][new_x] - tera[y][x] + 1
                else:
                    fuel = d[y][x] + 1
                if fuel < d[new_y][new_x]:
                    d[new_y][new_x] = fuel
                    Q.add((new_y,new_x))



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    tera = [list(map(int, input().split())) for _ in range(N)]

    #왼,아래,오,위
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    result = Dijkstra_custom(tera)

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
