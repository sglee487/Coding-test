# -*- coding: utf-8 -*-
import sys

sys.stdin = open("BOGGLE.txt", "r")

def is_possible(word, matrix):
    for r in range(5):
        for c in range(5):
            if word[0] == matrix[r][c]:
                if dfs(1, r,c, word):
                    return True

    return False

# 위 위오 오 오아 아 아왼 왼 왼위
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

def dfs(step, r, c, word):
    if step == len(word):
        return True
    for i in range(8):
        nr, nc = r + dy[i], c + dx[i]
        if 0<=nr<5 and 0<=nc<5:
            if word[step] == matrix[nr][nc]:
                if dfs(step+1,nr,nc,word):
                    return True
    return False


TEST_CASE = int(input())
for test_case in range(TEST_CASE):
    matrix = [input().strip() for _ in range(5)]

    candi_num = int(input())
    candidates = [input().strip() for _ in range(candi_num)]

    for cand in range(candi_num):
        if is_possible(candidates[cand], matrix):
            print(candidates[cand], "YES")
        else:
            print(candidates[cand], "NO")

    