def solution(str_list):
    for i in str_list :
        if i == "r" :
            return str_list[str_list.index("r")+1:]
        elif i == "l" :
            return str_list[:str_list.index("l")]
    return []