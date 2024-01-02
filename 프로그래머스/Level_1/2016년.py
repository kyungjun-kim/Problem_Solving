import datetime as dt
def solution(a, b):
    wd = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return wd[dt.datetime(2016,a,b).weekday()]