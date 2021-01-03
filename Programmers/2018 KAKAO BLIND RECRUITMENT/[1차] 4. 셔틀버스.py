def after_time(now,time):
    hour = int(now[:2])
    minute = int(now[3:])
    minute += time
    q, r = divmod(minute, 60)
    hour += q
    minute = r
    return "{:02d}:{:02d}".format(hour,minute)

def solution(n, t, m, timetable):
    timetable.sort()
    lastbus = after_time("09:00",(n-1)*t)
    for i in range(n):
        bustime = after_time("09:00",i*t)
        if len(timetable) < m: return lastbus
        # 마지막 버스에서 자리가 안남았기 때문에 경쟁. 꼴등보다 1분 빨리오기..
        if i == n-1:
            return min(after_time(timetable[m-1],-1),lastbus)
        for j in range(m):
            if timetable[0] > bustime:
                break
            else:
                timetable.pop(0)
    return

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]),"09:00")
print(solution(2,10,2,["09:10", "09:09", "08:00"]),"09:09")
print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"]),"08:59")
print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]),"00:00")
print(solution(1,1,1,["23:59"]),"09:00")
print(solution(10,60,45,["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]),"18:00")