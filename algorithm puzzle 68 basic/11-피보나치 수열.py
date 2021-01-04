def jarisum(n):
    return sum(map(int,list(str(n))))

fibo = [1,1]
while fibo[-1] != 144:
    fibo.append(fibo[-1]+fibo[-2])
print(fibo)
answer = []
while len(answer) < 5:
    fibo.append(fibo[-1] + fibo[-2])
    if fibo[-1] % jarisum(fibo[-1]) == 0:
        print(fibo[-1])
        answer.append(fibo[-1])