import datetime

nowday = datetime.datetime(1964,10,10)
print(nowday.isoformat)
while True:
    if nowday.year == 2020\
        and nowday.month == 7\
        and nowday.day == 25:
        break
    month = str(nowday.month) if nowday.month >= 10 else '0' + str(nowday.month)
    day = str(nowday.day) if nowday.day >= 10 else '0' + str(nowday.day)
    nowdayint = int(str(nowday.year) + month + day)
    daybin = '{0:b}'.format(nowdayint)
    daybinreverse = daybin[::-1]
    if daybin == daybinreverse:
        print(str(nowday.year) + month + day)
    nowday = nowday + datetime.timedelta(days=1)