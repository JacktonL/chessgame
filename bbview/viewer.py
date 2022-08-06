

def printboard(board):
        for i in board:
            print(" ---"*8)
            for j in i:
                print("|",j,end=" ")
            print("|")
        print(" ---"*8)

def getboard(num):
    b = bin(num)[::-1][:-2]
    n = ''
    for i in b:
            if i == '1':
                    n += 'X'
            else:
                    n += ' '
                    
    if len(n) < 64:
        f = 64-len(n)
        n += ' '*f
    l = []
    c = 0
    for i in range(8):
        t = []
        for j in range(8):
            t.append(n[c])
            c += 1
        l.append(t)
    return l[::-1]

while True:
    try:
        num = input("Input: ")
        num = int(num)
        b = getboard(num)
        printboard(b)
    except:
        print('\ninvalid input\n')
