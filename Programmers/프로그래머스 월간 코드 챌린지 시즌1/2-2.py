import numpy as np

def solution(arr):
    answer = [0,0]
    def is_all(ar):
        if all(map(all,ar)) == True:
            answer[1] += 1
            return True
        elif any(map(any,ar)) == False:
            answer[0] += 1
            return True
        else:
            return False
    def dfs(ar):
        if not is_all(ar):
            dfs(ar[:len(ar)//2,:len(ar)//2])
            dfs(ar[:len(ar)//2,len(ar)//2:])
            dfs(ar[len(ar)//2:,:len(ar)//2])
            dfs(ar[len(ar)//2:,len(ar)//2:])

    dfs(np.array(arr))
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]),[4,9])
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]),[10,15])