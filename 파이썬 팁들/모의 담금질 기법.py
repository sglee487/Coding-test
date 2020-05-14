# 파이썬 SW문제해결 응용_최적화 - 06 근사 알고리즘

# 전역 최소값 탐색
def Simulatd_Annealing():
    임의의 후보해 s를 선택한다.
    초기 T를 정한다.
    while True:
        for i in range(1, kt):
            s의 이웃해 중에서 랜덤하게 하나의 해 s`를 선택한다.
            d = s`의 값 - s의 값
            if d<0: s = s`
        else:
            q = (0,1) 사이에서 랜덤하게 선택한 수
        if q < p: s = s`
    T = aT
    if 종료 조건이 만족될 때까지 :
        break
    return s

cost_pre = infinite  # 이전 비용
T = 시작온도
while T > T_end:          # T_end가 될 때까지 반복
    cost_new = cost( )      # 비용 계산
    diff = cost_new – cost_prev    # 새로운 비용과 이전 비용의 차이
    if difference < 0 or  e(-diff/T) > random(0,1):
        cost_pre = cost_new    # 비용이 감소하거나 확률이 랜덤 값보다 더 크면 비용 갱신
    T = T * k                 # k : cooling factor