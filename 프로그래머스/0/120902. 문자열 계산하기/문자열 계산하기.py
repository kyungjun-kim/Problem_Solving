def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    for i,j in enumerate(my_string) :
        if j == "+" :
            answer += int(my_string[i+1])
        elif j == "-" :
            answer -= int(my_string[i+1])
    return answer