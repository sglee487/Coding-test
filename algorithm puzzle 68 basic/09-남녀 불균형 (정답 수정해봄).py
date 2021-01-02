boy, girl = 20, 10
boy, girl = boy + 1, girl + 1

ary = [0] * (boy * girl)
ary[0] = 1
matrix = [[0] * boy for _ in range(girl)]
# for g in range(girl):
#     matrix[g][0] = 1
# for b in range(boy):
#     matrix[0][b] = 1
matrix[0][0] = 1

for g in range(0, girl):
    for b in range(0, boy):
        if (b != g) and (boy - b != girl - g):
            if b > 0:
                ary[b + boy * g] += ary[b - 1 + boy * g]
            if g > 0:
                ary[b + boy * g] += ary[b + boy * (g-1)]
            matrix[g][b] = matrix[g-1][b] + matrix[g][b-1]

print(ary)
print(ary[-2], ary[-boy - 1])
print(ary[-2] + ary[-boy - 1])
print(*matrix,sep='\n')
print(matrix[girl-2][boy-1], matrix[girl-1][boy-2])
print(matrix[girl-2][boy-1] + matrix[girl-1][boy-2])