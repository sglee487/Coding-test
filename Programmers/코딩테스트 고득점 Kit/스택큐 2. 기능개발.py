def solution(progresses, speeds):
    # 0 in progress
    # 1 in ready to go
    # 2 already go
    real_progress = progresses[:]
    complete = [0] * len(progresses)
    total_complete = 0
    have_to_complete = len(progresses)
    answer = []
    in_one_complete = 0
    while total_complete < have_to_complete:
        for i in range(len(progresses)):
            if complete[i] >= 1: continue
            real_progress[i] += speeds[i]
            if real_progress[i] >= 100:
                complete[i] = 1
        for i in range(len(complete)):
            if complete[i] == 1:
                complete[i] = 2
                in_one_complete += 1
            elif complete[i] == 2:
                continue
            else:
                break
        if in_one_complete > 0:
            answer.append(in_one_complete)
            total_complete += in_one_complete
            in_one_complete = 0


    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))