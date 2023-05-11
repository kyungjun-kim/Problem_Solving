#문제링크 : https://www.acmicpc.net/problem/2720

N = int(input())
change = [25,10,5,1]
for i in range(N) :
    m = []
    price = int(input())
    for c in change :
        m.append(str(price // c))
        price %= c
    print(" ".join(m))