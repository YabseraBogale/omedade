import datetime


def giveTime():
    now=str(datetime.datetime.now()).split(',')[0].split('.')[0]
    return now

print(len(giveTime()))
print(giveTime())