# 날짜를 다루는 datatime 클래스 불러오기
from datetime import datetime, timedelta

# 기간 설정
start = datetime.strptime("1964-10-10","%Y-%m-%d")
end = datetime.strptime("2020-07-24","%Y-%m-%d")
step = timedelta(days=1)

# 해당하는 날짜 찾아 출력하기
while start <= end:
    day = bin(int(start.strftime("%Y%m%d"))).replace("0b","")
    if day == day[::-1]:
        print(start.strftime("%Y-%m-%d"))
    start += step