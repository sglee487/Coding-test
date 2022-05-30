from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("ALLERGY-1.txt", "r")

input = sys.stdin.readline


def search(friends, chosen):
    global best, n, m, foodFriendsDict, friendFoodList, foodCanFriendsList

    if chosen >= best: return

    first = 0
    for i in range(n):
        if friends[i] == 0:
            first = i
            break
        first += 1
    if first == n:
        best = min(best, chosen)
        return
    for food in friendFoodList[first]:
        for eatFood in foodCanFriendsList[food]:
            friends[eatFood] += 1
        search(friends, chosen+1)
        for eatFood in foodCanFriendsList[food]:
            friends[eatFood] -= 1

    return


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    friends = input().split()
    friendsDict = dict()
    for i, e in enumerate(friends):
        friendsDict[e] = i
    foodFriendsDict = defaultdict(list)
    friendFoodList = [[] for _ in range(n)]
    foodCanFriendsList = [[] for _ in range(m)]
    for i in range(m):
        tempInput = input().split()
        foodFriendsDict[i] = list(map(lambda x:friendsDict[x], tempInput[1:]))
        for friend in foodFriendsDict[i]:
            foodCanFriendsList[i].append(friend)
        for friend in tempInput[1:]:
            friendFoodList[friendsDict[friend]].append(i)

    best = m
    # print(f"{foodFriendsDict=}")
    # print(f"{friendFoodList=}")
    # print(f"{foodCanFriendsList=}")
    search([0]*n, 0)
    print(best)