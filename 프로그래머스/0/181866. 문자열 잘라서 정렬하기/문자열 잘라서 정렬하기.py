def solution(myString):
    return sorted(filter(lambda f : f!='', myString.split("x")))