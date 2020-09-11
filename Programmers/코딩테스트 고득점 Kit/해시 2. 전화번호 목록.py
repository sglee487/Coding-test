def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            minlen = min(len(phone_book[i]),len(phone_book[j]))
            if phone_book[i][:minlen] == phone_book[j][:minlen]: return False

    return True

print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))