import sys
input = sys.stdin.readline

# sys.stdin = open("17952-과제는 끝나지 않아!-1.txt", "r")

N = int(input())
work_list = []
total_score = 0
for n in range(N):
    com_line = list(map(int, input().split()))
    if com_line[0] == 1:
        work_list.append([com_line[1],com_line[2]])

    if not work_list: continue
    work_list[-1][1] -= 1
    if work_list[-1][1] == 0:
        total_score += work_list[-1][0]
        work_list.pop()

print(total_score)