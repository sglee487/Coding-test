import sys

sys.stdin = open("sample_input.txt", "r")

def merge(left, right):

    # 밑의 것은 이론에서 리스트를 사용할 경우의 병합과정이다.
    # 근데 시간이 너무 오래 결려 안되는 것 같다.
    # 리스트를 고정 길이로 만들기.
    # https://tothefullest08.github.io/algorithm/2019/08/31/1_5204_%EB%B3%91%ED%95%A9%EC%A0%95%EB%A0%AC/

    result = [0] * (len(left) + len(right))
    # 두 개의 분할된 리스트를 병합하여 result를 만듦
    i=0
    j=0
    while i < len(left) and j < len(right) :
        # 양쪽 리스트에 원소가 남아있는 경우
        # 두 서브 시르스틔 첫 원소들을 비교하여 작은 것부터 result에 추가함
        if left[i] <= right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i + j] = right[j]
            j += 1
    while i < len(left) :
        # 왼쪽 리스트에 원소가 남아있는 경우
        result[i+j] = left[i]
        i += 1
    while j < len(right) :
        # 오른쪽 리스트에 원소가 남아있는 경우
        result[i + j] = right[j]
        j += 1
    return result

    # 밑에가 원본. 위에가 개조 버전.

    # while len(left) > 0 and len(right) > 0 : # 양쪽 리스트에 원소가 남아있는 경우
    #     # 두 서브 시르스틔 첫 원소들을 비교하여 작은 것부터 result에 추가함
    #     if left[0] <= right[0]:
    #         result.append(left.pop(0))
    #     else:
    #         result.append(right.pop(0))
    # if len(left) > 0: # 왼쪽 리스트에 원소가 남아있는 경우
    #     result.extend(left)
    # if len(right) > 0: # 오른쪽 리스트에 원소가 남아있는 경우
    #     result.extend(right)
    # return result


def merge_sort(m):
    global iflgtr

    if len(m) <= 1:
        return m

    # 1. DIVIDE 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        iflgtr += 1

    # 2. CONQUER 부분 : 분할된 리스트들 병합
    return merge(left, right)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    L = list(map(int, input().split()))

    iflgtr = 0
    LS = merge_sort(L)

    print("#{}".format(test_case),LS[N//2], iflgtr)

    # ///////////////////////////////////////////////////////////////////////////////////
