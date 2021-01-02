boy, girl = 20, 10
boy, girl = boy + 1, girl + 1

ary = [0] * (boy * girl)
ary[0] = 1

for g in range(0, girl):
    for b in range(0, boy):
        if (b != g) and (boy - b != girl - g):
            if b > 0:
                ary[b + boy * g] += ary[b - 1 + boy * g]
            if g > 0:
                ary[b + boy * g] += ary[b + boy * (g-1)]

print(ary)
print(ary[-2] + ary[-boy - 1])