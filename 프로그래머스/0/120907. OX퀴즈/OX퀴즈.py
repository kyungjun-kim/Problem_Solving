def solution(quiz):
    answer = []
    for i in quiz :
        tmp = i.replace("- -","").replace("- ","-").replace("+ ","").split(" ")
        print(tmp)
        if int(tmp[0]) + int(tmp[1]) == int(tmp[-1]) :
            answer.append("O")
        else :
            answer.append("X")
    return answer