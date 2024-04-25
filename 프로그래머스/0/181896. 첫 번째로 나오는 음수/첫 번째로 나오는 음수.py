def solution(num_list):
    if len(list(filter(lambda f : f < 0 ,num_list))) > 0 :
        return num_list.index(list(filter(lambda f : f < 0 ,num_list))[0])
    else :
        return -1
    