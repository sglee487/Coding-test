def start(money):
    global result
    dfs(0, 0, 0,money)
    dfs(1, 1, 0,money)
    dfs(1, 2, 0,money)
    return

def dfs(start_index, index,total,money):
    global result
    if start_index == 0 and index >= len(money)-1:
        if total > result: result = total
        return
    if start_index == 1 and index >= len(money):
        if total > result: result = total
        return
    if start_index == 0:
        dfs(0, index+2,total + money[index],money)
        dfs(0, index+3,total + money[index],money)
    if start_index == 1:
        dfs(1, index+2,total + money[index],money)
        dfs(1, index+3,total + money[index],money)

    return

def solution(money):
    global result
    result = 0
    start(money)

    return result

print(solution([1, 2, 3, 1]),4)
print(solution([6, 7, 6, 4]),12)
print(solution([1,9,3,5,7,1,5]),21)
print(solution([1, 2, 3]),3)
print(solution([1, 2, 3, 1]),4)
print(solution([1, 2, 3, 1, 2]),5)
print(solution([1, 2, 3, 1, 2, 3]),6)
print(solution([1, 2, 3, 1, 2, 3, 4]),9)
print(solution([1,1,1]),1)
print(solution([1,1,1,1]),2)
print(solution([1,1,1,1,1]),2)
print(solution([1,1,1,1,1,1]),3)
print(solution([1,1,1,1,1,1,1]),3)
print(solution([1,1,1,1,1,1,1,1]),4)
print(solution([1,1,1,1,1,1,1,1,1]),4)
print(solution([1,1,1,1,1,1,1,1,1,1]),5)