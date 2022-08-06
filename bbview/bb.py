
def diagbl(n):
    sum = 0
    for i in range(n+1):
        sum += 2**(7*i+n)

    return sum

def diagtr(n):
    sum = 0
    for i in range(n+1):
        sum += 2**((63-n)-7*i)

    return sum

def diagtl(n):
    sum = 0
    for i in range(n+1):
        sum += 2**((56+n)-9*i)

    return sum

def diagbr(n):
    sum = 0
    for i in range(n+1):
        sum += 2**((7-n)+9*i)

    return sum


#print([[diagbr(i), bin(diagbr(i))] for i in range(8)])

def fac(n,f):
    n *= f
    if f < 2:
        return n
    return fac(n,f-1)

print(fac(900,899))


