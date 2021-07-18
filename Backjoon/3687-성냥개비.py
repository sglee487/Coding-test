import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("3687-성냥개비-4.txt", "r")

input = sys.stdin.readline

def calzeromin(n):
    if dpzeromin[n]:
        return dpzeromin[n]
    if n < 8:
        return dpzeromin[n]
    remain = n % 7
    if remain in (1,2,3,4,5,6):
        dpzeromin[n] = dpzeromin[6] + calzeromin(n-6)
    elif remain == 0:
        dpzeromin[n] = dpzeromin[7] + calzeromin(n-7)
    return dpzeromin[n]


def calmin(n):
    if dpmin[n]:
        return dpmin[n]
    if n <= 7:
        return dpmin[n]
    remain = n % 7
    if remain in (1,2):
        dpmin[n] = dpmin[2] + calzeromin(n-2)
    elif remain in (3,4,5):
        dpmin[n] = dpmin[5] + calzeromin(n-5)
    elif remain == 6:
        dpmin[n] = dpmin[6] + calzeromin(n-6)
    elif remain == 0:
        dpmin[n] = dpmin[7] + calzeromin(n-7)
    return dpmin[n]

def calmax(n):
    if dpmax[n]:
        return dpmax[n]
    if n >= 4:
        if n%2 == 1:
            dpmax[n] = dpmax[3] + calmax(n-3)
        else:
            dpmax[n] = dpmax[2] + calmax(n-2)
    return dpmax[n]

T = int(input())
for test_case in range(T):
    n = int(input())
    numchop = {0:6, 1:2, 2:5, 3:5, 4:4,
                5:5, 6:6, 7:3, 8:7, 9:6}
    chopnum = {2:[1], 3:[7], 4:[4], 5:[2,3,5],
               6:[0,6,9], 7:[8]}
    dpmin = [''] * (101)
    dpmin[2] = '1'
    dpmin[3] = '7'
    dpmin[4] = '4'
    dpmin[5] = '2'
    dpmin[6] = '0'
    dpmin[7] = '8'
    dpzeromin = [''] * 101
    dpzeromin[:8] = dpmin[:8]
    calzeromin(n)
    answermin = calmin(n)
    if answermin[0] == '0':
        answermin = '6' + answermin[1:]
    dpmax = [''] * (101)
    dpmax[2] = '1'
    dpmax[3] = '7'
    answermax = calmax(n)
    print(answermin, answermax)