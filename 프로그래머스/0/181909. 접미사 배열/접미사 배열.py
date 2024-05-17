def solution(my_string):
    answer = []
    for i,j in enumerate(my_string) :
        answer.append(my_string[i:])
    return sorted(answer)