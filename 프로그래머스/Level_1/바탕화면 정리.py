#문제풀이 : https://school.programmers.co.kr/learn/courses/30/lessons/161990
def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper[0])-1,len(wallpaper),0,0
    w = list(map(lambda x : list(tuple(x)), wallpaper))
    for i,j in enumerate(wallpaper) :
        if "#" in j and i < luy :
            luy = i
        if "#" in j and j.index("#") < lux :
            lux = j.index("#")
        if "#" in j[::-1] and len(j) - j[::-1].index("#") > rdx :
            rdx = len(j) - j[::-1].index("#")
        if "#" in j and i > rdy :
            rdy = i
    return [luy, lux, rdy+1, rdx]