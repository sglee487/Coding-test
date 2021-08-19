# 파이썬 SW문제해결 응용_최적화 - 01 문자열 탐색
# 2차시 02 문자열 매칭

# KMP 알고리즘
A:str = input().strip()
B:str = input().strip()
nextp = [-1] * len(B)

# p: 패턴, M: 패턴의 길이
# nextp: 불일치가 발생하면 이동할 위치를 저장
def KMP_Preprocess(p, nextp):
    M = len(p)
    i = 0; j = -1

    while i<M:
        nextp[i] = j
        while j >= 0 and p[i] != p[j]:
            j = nextp[j]

        i += 1; j += 1

KMP_Preprocess(B, nextp)

# t: 텍스트, p: 패턴
# N: 텍스트의 길이, M: 패턴의 길이
# nextp: 불일치가 발생하면 이동할 위치를 저장
def KMP_Search(t,p,nextp):
    N = len(t); M = len(p)
    i = 0; j = 0

    while i < N:
        while j >= 0 and t[i] != p[j]:
            j = nextp[j]
        i += 1; j += 1
        if j == M:
            return i-j
    return -1

print(1 if KMP_Search(A,B,nextp) != -1 else 0)



# 보이어 무어 알고리즘
# https://mungto.tistory.com/124
# 문자열 검색하는 보이어 무어 알고리즘
def boyer_moore(pattern, text):
    # 길이를 자주쓰므로 길이를 받아둔다.
    M = len(pattern)
    N = len(text)
    i = 0
    # 반복은 최대 긴텍스트 길이 - 작은텍스트 길이
    while i <= N - M:
        # 보이어 무어 알고리즘은 뒤에서부터 접근하므로 pattern길이의 -1을 해준다.
        # -1을 해주는 이유는 인덱스가 0부터 시작하기 때문이다.
        j = M - 1
        # 뒤에서부터 검사하고 인덱스를 감소하는 형식이므로 0보다 이상일때만 동작한다.
        while j >= 0:
            # 끝글자부터 비교하면서 같다면 하나씩 감소하면서 비교한다.
            if pattern[j] != text[i + j]:
                # 글자가 틀리다면 제일마지막 글자 기준으로 find 함수를 호출한다.
                move = find(pattern, text[i + M - 1])
                break
        j = j - 1
    # 인덱스가 -1이라는 뜻은 모든 글자가 맞았다는 이야기이다.
    if j == -1:
        # 찾았으므로 true를 리턴한다.
        return True
        # 인덱스 위치를 찾는다면
        # return i
    else:
        # -1이 아니라면 글자를 못찾은 것이므로 find에서 넘겨준 값만큼 옆으로 이동한다.
        i += move


# 여기까지 왔다면 끝까지 찾지 못한것이므로 False를 리턴한다.
return False


# 인데스 위치로 한다면
# return -1

# 불필요한 비교를 건너뛰기 위한 함수
def find(pattern, char):
    # 마지막 부분과 일치하는 부분이 있는지 검색한다.
    # 마지막 부분은 이미 가능성이 없으므로 그전부터 검사한다.
    for i in range(len(pattern) - 2, -1, -1):
        # 마지막글자와 패턴중 일치하는 숫자가 있다면 그만큼 이동한다.
        if pattern[i] == char:
            return len(pattern) - i - 1
    # 일치하는 글자가 없다면 패턴의 길이만큼 이동한다.
    return len(pattern)

str1 = "this is string example....wow!!!";
str2 = "is";

print str1.rindex(str2)
print str1.index(str2)

[1,2,3,2].index(2) # => 1
# 오른쪽부터 찾고 싶을땐 reverse로 바꿔서 쓰는 듯..


# 내가 만든거
A:str = input().strip()
B:str = input().strip()
skipdict = {b:v for b, v in zip(B, range(len(B)-1,-1,-1))}

def boyer_moore(A,B,skipdict):
    i = len(B)-1
    j = len(B)-1
    while i < len(A):
        if A[i] != B[j]:
            i += (skipdict[A[i]] if A[i] in skipdict else len(B))
            j = len(B)-1
        else:
            i -= 1
            j -= 1
            if j == -1:
                return i + 1
    return -1

print(1 if boyer_moore(A,B,skipdict) != -1 else 0)