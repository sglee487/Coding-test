import re


def betweens(time, timelines):
    count = 0
    start = time
    end = time + 1000
    for s, e in timelines:
        # 경우의 수를 생각하자..
        # s 왼 e 왼. 포함x
        # s 왼 e 안. 포함
        # s 왼 e 오. 포함
        # s 안 e 안. 포함
        # s 안 e 오. 포함
        # s 오 e 오. 포함x
        if e < start: continue
        if end <= s: continue
        count += 1
    return count


def solution(lines):
    timelines = []
    answer = 0
    for line in lines:
        l = re.search("2016-09-15 (\d+):(\d+):(\d+).(\d+) (\d+)\.?(\d+)?s", line)
        # ms 단위로 바꾸기
        endms = int(l.group(1)) * 3600 * 1000 + int(l.group(2)) * 60 * 1000 + int(l.group(3)) * 1000 + int(l.group(4))
        pms = int(l.group(5)) * 1000
        if l.group(6):
            pms += int(l.group(6))
        timelines.append((endms - pms + 1, endms))
    timelines.sort()
    n = len(timelines)
    maxcount = 0
    for i in range(n):
        maxcount = max(betweens(timelines[i][0], timelines), maxcount)
        maxcount = max(betweens(timelines[i][1], timelines), maxcount)

    return maxcount

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]),1)
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]),2)
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]),7)