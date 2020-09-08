def solution(gems):
    gem_len = len(set(gems))
    print(set(gems))

    answer = [0] * 2
    min_len = len(gems)

    start_index = 0
    end_index = len(gems)
    find = False
    while start_index <= len(gems) - gem_len:

        for index in range(start_index + gem_len, len(gems)+1):
            print(index, gems[start_index:index])
            if set(gems[start_index:index]) == set(gems):
                end_index = start_index + index
                find = True
                break
        if not(find): break
        for index in range(start_index, len(gems) - gem_len+1):
            print("start",index, gems[index:end_index])
            if set(gems[index:end_index]) != set(gems):
                start_index = index
                break

        if end_index - start_index < min_len:
            min_len = end_index - start_index
            answer[0], answer[1] = start_index, end_index

        start_index += 1
        end_index += 1
        find = False


    return answer