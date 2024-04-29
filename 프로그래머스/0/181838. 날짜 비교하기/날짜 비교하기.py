from datetime import datetime as dt
def solution(date1, date2):
    return int(dt(date1[0],date1[1],date1[2]) < dt(date2[0],date2[1],date2[2]))