def solution(a, d, included):
    return sum(list(map(lambda x,y : x if y else 0 , [a + x*d for x in range(len(included))] ,included)))