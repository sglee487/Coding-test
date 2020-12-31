numbers = list(range(1,101))
show = [False] * 101
for i in range(2,101):
    for j in range(i,101,i):
        show[j] = not(show[j])

print(show)
for i in range(1,101):
    if not show[i]: print(i)