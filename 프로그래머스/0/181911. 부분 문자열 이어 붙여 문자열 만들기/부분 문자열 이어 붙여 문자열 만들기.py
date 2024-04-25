def solution(my_strings, parts):
    return ''.join(list(map(lambda x,y : x[y[0]:y[1]+1],my_strings,parts)))