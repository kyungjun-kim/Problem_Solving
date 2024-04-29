def solution(my_string, indices):
    return ''.join([my_string[x] if x not in indices else '' for x in range(len(my_string))])