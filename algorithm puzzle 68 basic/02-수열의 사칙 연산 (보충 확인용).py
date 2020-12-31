import re

ts = '3+05+2'
nts = re.sub(r"0(\d+)",r"\1",ts)
print(nts)