def solution(intStrs, k, s, l):
    return list(filter(lambda f : f > k, map(lambda x : int(x[s:s+l]), intStrs)))