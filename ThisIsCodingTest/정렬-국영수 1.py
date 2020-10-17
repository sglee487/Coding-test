import sys

sys.stdin = open("정렬-국영수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Student = []
    for _ in range(N):
        name, guk, eng, math = sys.stdin.readline().split()
        Student.append((name,int(guk),int(eng),int(math)))
    student_name = []
    for i in sorted(Student,key=lambda x:(-x[1],x[2],-x[3],x[0])):
        student_name.append(i[0])
    print(*student_name,sep='\n')
