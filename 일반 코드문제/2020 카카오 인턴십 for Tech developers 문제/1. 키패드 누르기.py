def where_yx(number):
    if number == 1:
        return (0, 0)
    if number == 2:
        return (0, 1)
    if number == 3:
        return (0, 2)
    if number == 4:
        return (1, 0)
    if number == 5:
        return (1, 1)
    if number == 6:
        return (1, 2)
    if number == 7:
        return (2, 0)
    if number == 8:
        return (2, 1)
    if number == 9:
        return (2, 2)
    if number == 0:
        return (3, 1)


def solution(numbers, hand):
    left_yx = (3,0)
    right_yx = (3,2)
    result = []
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            left_yx = where_yx(num)
            result.append("L")
        if num == 3 or num == 6 or num == 9:
            right_yx = where_yx(num)
            result.append("R")
        if num == 2 or num == 5 or num == 8 or num == 0:
            r, c = where_yx(num)
            disl = abs(left_yx[0] - r) + abs(left_yx[1] - c)
            disr = abs(right_yx[0] - r) + abs(right_yx[1] - c)
            print(num)
            print("disl: {}, disr: {}".format(disl,disr))
            if disl < disr:
                left_yx = where_yx(num)
                result.append("L")
            if disr < disl:
                right_yx = where_yx(num)
                result.append("R")
            if disl == disr:
                if hand == "left":
                    left_yx = where_yx(num)
                    result.append("L")
                if hand == "right":
                    right_yx = where_yx(num)
                    result.append("R")

    answer = ''.join(result)
    print(answer)
    return answer