def solution(n):
    return sum([x if n%2 else x**2 for x in range(int(n%2),n+1,2)])