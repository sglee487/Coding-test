import sys

sys.stdin = open("input2.txt", "r")

def solve():
    global min_room, max_distance

    # 왼쪽, 아래, 오른쪽, 위
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    Q = []
    for room_number, r, c in room_numbers:
        if not visited[r][c]:
            Q.append((r, c, 1))
        while Q:
            qr, qc, cd = Q.pop()
            visited[qr][qc] = True
            if cd >= max_distance:
                if cd == max_distance:
                    min_room = min(min_room, room_number)
                else:
                    max_distance = cd
                    min_room = room_number

            for d in range(4):
                y = qr + dy[d]
                x = qc + dx[d]
                if not(0 <= x < N and 0 <= y < N) or visited[y][x]:
                    continue
                if room[y][x] == room[qr][qc] + 1:
                    Q.append((y, x, cd + 1))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    room = []
    for _ in range(N):
        room.append(list(map(int,input().split())))

    room_numbers = []
    for r in range(N):
        for c in range(N):
            room_numbers.append((room[r][c], r, c))
    room_numbers = sorted(room_numbers, key=lambda x: x[0])

    visited = [[False] * N for _ in range(N)]

    min_room = N*N
    max_distance = 1
    # 309 ms
    solve()

    print("#{}".format(test_case), min_room,max_distance)
    # ///////////////////////////////////////////////////////////////////////////////////
