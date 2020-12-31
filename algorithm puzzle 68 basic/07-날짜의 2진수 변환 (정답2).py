# 날짜를 다루는 datatime 클래스 불러오기
from datetime import datetime, timedelta

# 대상 기간에서 2진수의 5번째 문자부터 8개의 문자 추출
from_left = int(bin(19641010).replace("0b","")[4:4 + 8], 2)
to_left = int(bin(20200724).replace("0b","")[4:4 + 8], 2)
print(from_left,to_left)

# 좌우의 8문자를 반복
for i in range(from_left, to_left + 1):
    l = "{0:08b}".format(i) # 왼쪽
    r = l[::-1] # 오른쪽
    for m in range(0, 1 + 1): # 중앙
        value = "1001{}{}{}1001".format(l, m, r)
        try:
            # 변환 가능한지 확인
            date = datetime.strptime(str(int(value, 2)), "%Y%m%d")
            # 변환 가능할 경우 출력
            print(date.strftime("%Y-%m-%d"))
        except:
            pass