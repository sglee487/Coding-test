from itertools import permutations

def solution(n, weak, dist):
    extendweak = weak[:]
    for w in weak:
        extendweak.append(n+w)
    minfriends = 99
    flen = len(dist)
    wlen = len(weak)
    for friends in permutations(dist,len(dist)):
        for wall_start_index in range(wlen):
            friend_index = 0
            now = extendweak[wall_start_index]
            for w in extendweak[wall_start_index:wall_start_index+wlen]:
                if now+friends[friend_index] < w:
                    now = w
                    friend_index += 1
                    if friend_index == flen:
                        break
            if friend_index != flen:
                minfriends = min(minfriends,friend_index+1)

    if minfriends == 99:
        return -1
    else:
        return minfriends


print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]),2)
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]),1)