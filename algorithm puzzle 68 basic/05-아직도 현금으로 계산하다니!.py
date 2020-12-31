possible_case = 0

money = 1000

for i in range(16):
    for j in range(16):
        for k in range(16):
            for l in range(16):
                if i+j+k+l > 15: continue
                allsum = (i*500 + j * 100 + k*50 + l*10)
                if allsum == money:
                    print(i,j,k,l)
                    possible_case += 1
                elif allsum > money:
                    break

print(possible_case)