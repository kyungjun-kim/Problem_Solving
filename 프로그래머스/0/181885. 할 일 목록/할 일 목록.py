def solution(todo_list, finished):
    return list(filter(lambda f : f != '', map(lambda x,y : x*int(not(y)), todo_list, finished)))