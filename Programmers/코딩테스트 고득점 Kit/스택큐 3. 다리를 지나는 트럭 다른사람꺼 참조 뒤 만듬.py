from collections import deque

def solution(bridge_length, weight, truck_weights):

    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)

    cur_weight = 0
    time = 0
    while truck:
        outtruck = bridge.popleft()
        if outtruck > 0:
            cur_weight -= outtruck

        intotruck = truck[0]
        if cur_weight + intotruck <= weight:
            cur_weight += intotruck
            bridge.append(truck.popleft())
        else:
            bridge.append(0)

        time += 1

    while bridge:
        bridge.popleft()
        time += 1

    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))