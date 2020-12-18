# https://programmers.co.kr/learn/courses/30/lessons/60061

def isright(answer):
    for x, y, a in answer:
        # 기둥일 경우
        if a == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer: continue
            if [x,y-1,0] in answer: continue
            else:
                return False
        # 보일 경우
        elif a == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer: continue
            if [x-1,y,1] in answer and [x+1,y,1] in answer: continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 구조물 삭제
        if b == 0:
            answer.remove([x, y, a])
            if not isright(answer):
                answer.append([x, y, a])
        # 구조물 설치
        elif b == 1:
            answer.append([x,y,a])
            if not isright(answer):
                answer.remove([x,y,a])
        print(answer)
    answer.sort()
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]),[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]])
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]),[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]])