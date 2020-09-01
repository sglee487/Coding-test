# 입력 사이에 공간이 있을때
list(map(int,input().split()))

# 입력 사이에 공간이 없을때
list(input())
board = [input() for _ in range(N)]

# 행렬 만들기
visited = [[0] * N for _ in range(N)]

# 정렬 기준 방법
room_numbers = sorted(room_numbers, key=lambda x: -x[1])

# 행렬 뒤집기
N, M = map(int, input().split())
HR = [0 for _ in range(N)]
for i, c in enumerate(zip(*H)):
    HR[i] = list(c)