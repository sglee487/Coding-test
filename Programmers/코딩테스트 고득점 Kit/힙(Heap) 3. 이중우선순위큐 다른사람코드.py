# peacecheejecake
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]

print(solution(["I 16","D 1"]),[0,0])
print(solution(["I 7","I 5","I -5","D -1"]),[7,5])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]),[333, -45])
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]), [0, 0])