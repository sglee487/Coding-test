def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            print(red,i,red//i)
            if 2*(i + red//i) == brown-4: # 2*(i + red//i) 둘레의 길이
                return [red//i+2, i+2]

print(solution(10,2),[4,3])
print(solution(8,1),[3,3])
print(solution(24,24),[8,6])