a, b = map(int, input().strip().split(' '))
c = ''
for i in range(b) :
    for i in range(a) :
        c += '*'
    print(c)
    c = ''