def solution(cacheSize, cities):
    if cacheSize == 0: return 5 * len(cities)
    cities = [e.lower() for e in cities]
    total_time = 0
    LRUstack = []
    for city in cities:
        if city in LRUstack:
            LRUstack.pop(LRUstack.index(city))
            total_time += 1
        else:
            if len(LRUstack) == cacheSize:
                LRUstack.pop(0)
            total_time += 5
        LRUstack.append(city)
    return total_time

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]),50)
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]),21)
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]),60)
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]),52)
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]),16)
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]),25)
