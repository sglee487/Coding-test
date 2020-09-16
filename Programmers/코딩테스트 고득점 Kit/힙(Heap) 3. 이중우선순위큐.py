def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > data[mid]:
            start = mid + 1
        if target < data[mid]:
            end = mid - 1
    mid = (start + end) // 2
    return mid + 1

def solution(operations):
    L = []
    for s in operations:
        command, number = s.split()
        number = int(number)
        if command == "I":
            if not L:
                L.append(number)
            else:
                if number <= L[0]:
                    L.insert(0, number)
                elif number >= L[-1]:
                    L.insert(len(L), number)
                else:
                    L.insert(binary_search(number, L), number)
        if command == "D":
            if not L:
                pass
            elif number == 1:
                del L[-1]
            elif number == -1:
                del L[0]
    print(L)
    if not L:
        return [0, 0]
    else:
        return [L[-1], L[0]]

print(solution(["I 16","D 1"]),[0,0])
print(solution(["I 7","I 5","I -5","D -1"]),[7,5])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]),[333, -45])
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]), [0, 0])