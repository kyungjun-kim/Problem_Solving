def solution(myStr):
    answer = list(filter(lambda f : f!= '', myStr.replace("a",'_').replace("b","_").replace("c","_").split("_")))
    return answer if len(answer) > 0 else ["EMPTY"]