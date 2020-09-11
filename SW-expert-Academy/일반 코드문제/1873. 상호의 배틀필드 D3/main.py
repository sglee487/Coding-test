import sys

sys.stdin = open("input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    H, W = map(int, input().split())
    Map = []
    for _ in range(H):
        Map.append(list(input()))
    _ = input()
    inpl = list(input())

    # print(*Map,sep='\n')
    # print(inpl)

    tank_y, tank_x, tank_d = -1, -1, ''
    for r in range(H):
        for c in range(W):
            if Map[r][c] == '<' or Map[r][c] == '>' or Map[r][c] == '^' or Map[r][c] == 'v':
                tank_y, tank_x, tank_d = r, c, Map[r][c]
                break
        if tank_y != -1 and tank_x != -1: break

    for inp in inpl:
        if inp == 'S':
            if tank_d == '<':
                po_x = tank_x
                po_x -= 1
                while po_x >= 0:
                    # if Map[tank_y][po_x] == '.':
                    #     continue
                    if Map[tank_y][po_x] == '*':
                        Map[tank_y][po_x] = '.'
                        break
                    if Map[tank_y][po_x] == '#':
                        break
                    po_x -= 1
            if tank_d == '>':
                po_x = tank_x
                po_x += 1
                while po_x < W:
                    # if Map[tank_y][po_x] == '.':
                    #     continue
                    if Map[tank_y][po_x] == '*':
                        Map[tank_y][po_x] = '.'
                        break
                    if Map[tank_y][po_x] == '#':
                        break
                    po_x += 1
            if tank_d == '^':
                po_y = tank_y
                po_y -= 1
                while po_y >= 0:
                    # if Map[po_y][tank_x] == '.':
                    #     continue
                    if Map[po_y][tank_x] == '*':
                        Map[po_y][tank_x] = '.'
                        break
                    if Map[po_y][tank_x] == '#':
                        break
                    po_y -= 1
            if tank_d == 'v':
                po_y = tank_y
                po_y += 1
                while po_y < H:
                    # if Map[po_y][tank_x] == '.':
                    #     continue
                    if Map[po_y][tank_x] == '*':
                        Map[po_y][tank_x] = '.'
                        break
                    if Map[po_y][tank_x] == '#':
                        break
                    po_y += 1
        if inp == 'U':
            tank_d = '^'
            if tank_y - 1 < 0:
                Map[tank_y][tank_x] = '^'
                continue
            if Map[tank_y-1][tank_x] == '*' or Map[tank_y-1][tank_x] == '#' or Map[tank_y-1][tank_x] == '-':
                Map[tank_y][tank_x] = '^'
                continue
            Map[tank_y - 1][tank_x], Map[tank_y][tank_x] = '^', '.'
            tank_y = tank_y - 1
        if inp == 'D':
            tank_d = 'v'
            if tank_y + 1 >= H:
                Map[tank_y][tank_x] = 'v'
                continue
            if Map[tank_y+1][tank_x] == '*' or Map[tank_y+1][tank_x] == '#' or Map[tank_y+1][tank_x] == '-':
                Map[tank_y][tank_x] = 'v'
                continue
            Map[tank_y + 1][tank_x], Map[tank_y][tank_x] = 'v', '.'
            tank_y = tank_y + 1
        if inp == 'L':
            tank_d = '<'
            if tank_x - 1 < 0:
                Map[tank_y][tank_x] = '<'
                continue
            if Map[tank_y][tank_x-1] == '*' or Map[tank_y][tank_x-1] == '#' or Map[tank_y][tank_x-1] == '-':
                Map[tank_y][tank_x] = '<'
                continue
            Map[tank_y][tank_x-1], Map[tank_y][tank_x] = '<', '.'
            tank_x = tank_x - 1
        if inp == 'R':
            tank_d = '>'
            if tank_x + 1 >= W:
                Map[tank_y][tank_x] = '>'
                continue
            if Map[tank_y][tank_x+1] == '*' or Map[tank_y][tank_x+1] == '#' or Map[tank_y][tank_x+1] == '-':
                Map[tank_y][tank_x] = '>'
                continue
            Map[tank_y][tank_x+1], Map[tank_y][tank_x] = '>', '.'
            tank_x = tank_x + 1
        # print(inp)
        # print(*Map, sep='\n')


    print("#{}".format(test_case),end=' ')
    print(*Map[0],sep='')
    for i in range(1,H):
        print(*Map[i], sep='')
    # ///////////////////////////////////////////////////////////////////////////////////
