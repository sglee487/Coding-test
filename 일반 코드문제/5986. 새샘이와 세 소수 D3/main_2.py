import sys

sys.stdin = open("s_input2.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                     211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                     401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                     503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                     601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                     701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                     809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                     907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    goal = int(input())
    count = 0

    onesame_count = 0
    twosame_count = 0
    threesame_count = 0

    for first_index in range(len(prime_numbers)):
        for second_index in range(len(prime_numbers)):
            for third_index in range(len(prime_numbers)):
                result = prime_numbers[first_index] + prime_numbers[second_index] + prime_numbers[third_index]
                if result == goal:
                    count += 1
                    # print(first_index,second_index,third_index)
                    if first_index == second_index == third_index:
                        threesame_count += 1
                        break
                    if (first_index == second_index or first_index == third_index
                        or second_index == third_index):
                        twosame_count += 1
                        break
                    onesame_count += 1
                    break
                if result > goal:
                    break

    count_result = threesame_count + (twosame_count // 3) + (onesame_count // 6)

    print("#{}".format(test_case), count_result)

    # ///////////////////////////////////////////////////////////////////////////////////
