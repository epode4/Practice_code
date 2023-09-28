import datetime

def solution(a, b):
    week = ['MON', 'TUE', 'WED','THU','FRI','SAT','SUN']
    answer = datetime.datetime.strptime('2016'+str(a)+str(b),'%Y%m%d')
    return (week[answer.weekday()])
    