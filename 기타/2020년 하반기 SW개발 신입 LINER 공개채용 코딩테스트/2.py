from collections import deque

def solution(ball, order):
    ballnum = len(ball)
    orderq = deque(order)
    ballq = deque(ball)
    combuf = []
    outballs = []

    while len(outballs) < ballnum or len(orderq) != 0:
        new_order = orderq.popleft()
        if new_order == ballq[0]:
            outballs.append(ballq.popleft())
        elif new_order == ballq[-1]:
            outballs.append(ballq.pop())
        else:
            combuf.append(new_order)

        while len(combuf) != 0 and (ballq[0] in combuf or ballq[-1] in combuf):
            if ballq[0] in combuf:
                comin = combuf.index(ballq[0])
                outballs.append(ballq.popleft())
                del combuf[comin]
            elif ballq[-1] in combuf:
                comin = combuf.index(ballq[-1])
                outballs.append(ballq.pop())
                del combuf[comin]

    return outballs

print(solution([1, 2, 3, 4, 5, 6],[6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24],[9, 2, 13, 24, 11]))