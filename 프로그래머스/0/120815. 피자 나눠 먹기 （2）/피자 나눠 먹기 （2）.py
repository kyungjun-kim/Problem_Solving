def solution(n):
    for i in range(min(6,n),0, -1) :
        if 6 % i == 0 and n % i == 0 :
            print(i)
            a = i
            return (6 * n)/a/6
            break