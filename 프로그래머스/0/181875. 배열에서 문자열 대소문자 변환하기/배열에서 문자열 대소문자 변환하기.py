def solution(strArr):
    return list(map(lambda x,y : x.upper() if y % 2  else x.lower() , strArr,range(len(strArr))))