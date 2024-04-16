def solution(numlist, n):
    answer = list(map(lambda x : [x,x-n], numlist))
    answer = sorted(answer, key = lambda x : [abs(x[1]),-x[1]])
    return list(map(lambda x : x[0], answer))