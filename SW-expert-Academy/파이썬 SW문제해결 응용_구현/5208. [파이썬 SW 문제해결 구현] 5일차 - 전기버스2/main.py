import sys

sys.stdin = open("sample_input.txt", "r")

def gobus(start_index,step, end_index):
    global scn
    print("start_index" , start_index,"step",step,"end_index",end_index)
    if step > scn:
        return
    elif start_index >= end_index:
        print("end.. step",step, "scn",scn)
        if step < scn:
            scn = step
            print("scn",scn)
    else:
        for i in range(start_index+N[start_index],start_index,-1):
            gobus(i,step+1,end_index)


    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = list(map(int, input().split()))[1:]
    # print(N)

    scn = len(N)-1
    gobus(0,0,len(N))

    print("#{}".format(test_case),scn-1)

    # ///////////////////////////////////////////////////////////////////////////////////
