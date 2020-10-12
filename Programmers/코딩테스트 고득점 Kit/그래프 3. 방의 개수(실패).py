def solution(arrows):
    ardict = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1),
              4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}
    acorstack = [(0,0)]
    result = 0
    r,c = 0,0
    inline = False
    for ar in arrows:
        r += ardict[ar][0]
        c += ardict[ar][1]
        if (r,c) in acorstack:
            inline = True
        acorstack.append((r, c))

        r += ardict[ar][0]
        c += ardict[ar][1]
        if (r, c) in acorstack and inline == False:
            result += 1
        acorstack.append((r, c))
        r += ardict[ar][0]
        c += ardict[ar][1]
        acorstack.append((r, c))

        r += ardict[ar][0]
        c += ardict[ar][1]
        if (r, c) in acorstack and inline == False:
            result += 1
        acorstack.append((r, c))

        # print(acorstack,result)

    return result

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]),3)
print(solution([2,7,2,5]),2)
print(solution([2,7,2,5,0]),3)
print(solution([1,1,4,4,6,6,1,7,3]),1)