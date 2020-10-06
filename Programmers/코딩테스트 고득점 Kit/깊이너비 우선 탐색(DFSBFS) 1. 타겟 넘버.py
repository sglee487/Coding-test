def dfs(index,total_sum,numbers,target):
    global result
    if index == len(numbers):
        if total_sum == target: result += 1
        return
    dfs(index+1,total_sum + numbers[index],numbers,target)
    dfs(index+1,total_sum - numbers[index],numbers,target)

def solution(numbers, target):
    global result
    result = 0
    dfs(0,0,numbers,target)
    return result

print(solution([1, 1, 1, 1, 1],3),5)