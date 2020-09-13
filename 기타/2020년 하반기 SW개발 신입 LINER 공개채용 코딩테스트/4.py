def is_empty_board(r,c,maze,N):
    if 0 <= r < N and 0 <= c < N:
        if maze[r][c] == 0:
            return True
        else:
            return False
    else: return False

def solution(maze):
    # 행렬 방향
    # 왼쪽, 아래, 오른쪽, 위
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    dir = 3
    person = [0,0,dir]
    N = len(maze)
    movecount = 0
    while [person[0],person[1]] != [N-1, N-1]:
        if is_empty_board(person[0] + dy[(person[2]+1)%4],person[1] + dx[(person[2]+1)%4],maze,N):
            person[2] = (person[2]+1)%4
        while not(is_empty_board(person[0] + dy[person[2]],person[1] + dx[person[2]],maze,N)):
            person[2] = (person[2]-1)%4
        person[0] = person[0] + dy[person[2]]
        person[1] = person[1] + dx[person[2]]
        movecount+=1

    return movecount

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))