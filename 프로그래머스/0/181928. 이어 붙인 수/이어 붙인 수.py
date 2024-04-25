def solution(num_list):
    return int("".join([str(x) if x%2 else "" for x in num_list])) + int("".join([str(x) if x%2 == 0 else "" for x in num_list]))