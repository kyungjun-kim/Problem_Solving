def solution(str_list, ex):
    return "".join(list(filter(lambda f : ex not in f, str_list)))