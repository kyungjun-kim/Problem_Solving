def solution(numbers):
    answer = list(map(lambda x : str(x), numbers))
    return str(int(''.join(sorted(answer , key = lambda x : [x[0] , x*4], reverse = True))))