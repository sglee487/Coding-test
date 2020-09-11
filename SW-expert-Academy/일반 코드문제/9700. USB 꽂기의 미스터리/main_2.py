# Test Case
tc = input()
result_list = []

for i in range(int(tc)):
    data = input()
    data = data.split(' ')

    # 올바른 면으로 USB를 꽂을 확률
    p = float(data[0])
    # 올바른 면으로 꽂을 시 정상적으로 USB가 꽂힐 확률
    q = float(data[1])

    s1 = (1 - p) * q
    s2 = (p * (1 - q) * q)

    result_string = 'YES' if s1 < s2 else 'NO'
    result_list.append(f'#{i + 1} {result_string}')

for r in result_list:
    print(r)