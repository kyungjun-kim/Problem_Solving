def solution(arr, delete_list):
    return list(filter(lambda f : f not in delete_list, arr))