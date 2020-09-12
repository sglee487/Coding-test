from collections import deque

def solution(bridge_length, weight, truck_weights):
    goc = deque()
    going = deque()
    standby = deque(truck_weights)
    time = 1
    curcanweight = weight
    while len(goc) < len(truck_weights):
        time += 1
        if len(standby) != 0:
            waitingtruck = standby[0]
        else:
            waitingtruck = -1
        if waitingtruck == -1:
            pass
        elif curcanweight >= waitingtruck:
            going.append([waitingtruck,bridge_length])
            curcanweight -= waitingtruck
            standby.popleft()
        for i in range(len(going)):
            going[i][1] -= 1
        if going[0][1] == 0:
            comtruck = going[0][0]
            goc.append(going.popleft()[0])
            curcanweight += comtruck

    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))