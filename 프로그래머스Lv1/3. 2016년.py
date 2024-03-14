import datetime

def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    num = datetime.datetime(2016, a, b).weekday()
    return day[num]
