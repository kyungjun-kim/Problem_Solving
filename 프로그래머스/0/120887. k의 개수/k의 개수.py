def solution(i, j, k):
    return "".join(list(map(lambda x : str(x), range(i,j+1)))).count(str(k))