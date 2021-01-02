N = 12

def move(log):
    # 맨 처음의 위치를 포함하여 N+1개 조사하면 종료
    if len(log) == N + 1:
        return 1
    
    cnt = 0
    # 전후 좌우로 이동
    for d in [[0,1], [0,-1], [1,0], [-1,0]]:
        # 탐색이 끝나지 않았으면 이동시킴
        next_pos = [log[-1][0] + d[0], log[-1][1] + d[1]]
        # # 로그에 다음 위치가 기록되어 있는지 확인하기
        # check = False
        # for p in log:
        #     if p[0] == next_pos[0] and p[1] == next_pos[1]:
        #         check = True # 있는 경우 플래그를 True로 변경
        # if check == False:
        #     cnt += move(log + [next_pos])
        if [next_pos[0],next_pos[1]] not in log:
            cnt += move(log + [next_pos])
    return cnt

print(move([[0,0]]))