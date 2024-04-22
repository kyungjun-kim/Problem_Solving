def solution(my_string):
    my_string = list(map(lambda x : x if x.isdigit() else "_" ,my_string))
    return sum(list(map(lambda x : int(x) if x.isdigit() else 0, "".join(my_string).split("_"))))