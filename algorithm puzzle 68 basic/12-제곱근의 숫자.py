def allnumlen(s):
    alset = set()
    for i, c in enumerate(s,1):
        alset.add(c)
        if len(alset) == 10:
            return i
    return 52

minjulen = 100
minsolen = 100
minju = 999999
minso = 999999
for i in range(2,1000000):
    aljunset = {}
    alsonset = {}
    s = "{:0.52f}".format(i ** (1/2))
    ju = s.replace('.','')
    so = s.split('.')[1]
    jul = allnumlen(ju)
    if jul < minjulen:
        minjulen = jul
        minju = i
    sol = allnumlen(so)
    if sol < minsolen:
        minsolen = sol
        minso = i
print(minju,minjulen)
print(minso,minsolen)