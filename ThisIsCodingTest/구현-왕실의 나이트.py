def solution(s):
    count = 0
    # 위왼 위오 오위 오아 아왼 아오 왼위 왼아
    dy = [-2,-2,-1,1,2,2,-1,1]
    dx = [-1,1,2,2,-1,1,-2,-2]
    c = s[0]
    r = s[1]
    for i in range(8):
        nr, nc = int(r) + dy[i], ord(c) + dx[i]
        if 1 <= nr <= 8 and ord('a') <= nc <= ord('h'):
            count += 1
    return count

print(solution('a1'),2)