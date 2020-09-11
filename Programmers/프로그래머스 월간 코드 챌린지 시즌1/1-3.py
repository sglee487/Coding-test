def solution(a):
    answer = sorted(a)
    print(len(a))
    surround = []
    leftcount = 0
    rightcount = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i > j:
                if a[j] < a[i]: leftcount += 1
            if a[i] == a[j]: continue
            if i < j:
                if a[j] < a[i]: rightcount += 1
        print(a[i], leftcount, rightcount, end="  ")
        surround.append((a[i],leftcount,rightcount))
        leftcount = 0
        rightcount = 0
    surround = sorted(surround, key=lambda x:x[0])
    print()
    print(surround)
    return answer

print(solution([9,-1,-5])) # 3
print(solution([-1,9,-5]))
# -5 -1
print(solution([3, 9,-1,-5])) # 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # 6