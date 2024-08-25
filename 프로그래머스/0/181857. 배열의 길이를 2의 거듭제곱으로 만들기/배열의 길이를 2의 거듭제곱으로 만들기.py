def solution(arr):
    a,cnt = len(arr),0
    while a % 2 == 0 :
        a /= 2
        cnt += 1
    if a != 1 :
        while 2**cnt < len(arr) :
            cnt += 1
            print(2**cnt)
        for i in range(2**cnt-len(arr)) :
            arr.append(0)
    return arr