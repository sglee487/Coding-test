from collections import deque

cnt = 0
def change(target, coins, usable):
    global cnt
    coin = coins.popleft()
    if len(coins) == 0:
        if target // coin <= usable:
            cnt += 1
    else:
        for i in range(0, target // coin + 1):
            change(target - coin * i, coins.copy(), usable - i)

change(1000, deque([500,100,50,10]), 15)
print(cnt)