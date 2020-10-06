from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    def is_possible_change(bcw,tcw):
        count = 0
        for b,t in zip(bcw,tcw):
            if b==t: count += 1
        return True if count == len(bcw)-1 else False
    visited = [False] * len(words)
    Q = deque()
    Q.append((0,begin,visited[:]))
    result = 0
    while Q:
        step, word, visited = Q.popleft()
        if word == target:
            result = step
            break
        for i, w in enumerate(words):
            if visited[i]: continue
            visited[i] = True
            if is_possible_change(word,w):
                Q.append((step+1,w,visited[:]))
            visited[i] = False

    return result

print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']),4)
print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log']),0)