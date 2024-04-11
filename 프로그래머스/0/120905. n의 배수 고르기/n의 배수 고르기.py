def solution(n, numlist):
    return list(filter(lambda f : f % n == 0, numlist))