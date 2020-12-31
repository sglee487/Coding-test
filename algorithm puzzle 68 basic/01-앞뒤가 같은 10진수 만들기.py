num = 11
while True:
    if str(num) == str(num)[::-1]\
        and "{0:b}".format(num) == "{0:b}".format(num)[::-1]\
        and "{0:o}".format(num) == "{0:o}".format(num)[::-1]:
        break
    num += 2
print(num)